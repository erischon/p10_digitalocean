from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


from database.models import Product, Nutriscore


class UsersTestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.admin_user = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@test.com',
            password='test123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@test.com',
            password='test123',
            username='testuser'
        )

        self.factory = RequestFactory()

        nutriscore = Nutriscore.objects.create(nut_id=1, nut_type="C")
        self.product = Product.objects.create(
            prod_id=3017620422003,
            prod_name="test product",
            nut_id=nutriscore,
        )
        self.product.myproduct.add(self.user)

        self.signupuser_url = reverse('signupuser')
        self.logoutuser_url = reverse('logoutuser')
        self.moncompte_url = reverse('moncompte')
        self.myproducts_url = reverse('myproducts')
        self.myproducts_delete_url = reverse(
            'myproducts_delete', args=[self.product.prod_id])
        self.password_reset_url = reverse('password_reset')

    # === Method signupuser ===

    def test_signupuser_view(self):
        response = self.client.get(self.signupuser_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_signupuser_view_post_method_no_same_kw(self):
        response = self.client.post(
            '/users/signup/', {'password1': 'pass1', 'password2': 'pass2'})

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_signupuser_view_post_method_except(self):
        self.client.logout()
        response = self.client.post('/users/signup/', {'password1': 'pass1', 'password2': 'pass1', 'username': 'testuser', 'email': 'testemail'})

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_signupuser_view_post_method_with_connect(self):
        self.client.logout()
        response = self.client.post(
            '/users/signup/', 
            {
                'password1': 'pass1', 
                'password2': 'pass1', 
                'username': 'testuser2', 
                'email': 'testemail@test.com'
            }
        )

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/users/moncompte/')

    # === Method loginuser ===

    def test_loginuser_view(self):
        response = self.client.post(
            '/users/login/', 
            {'username': 'test@test.com', 'password': 'test123'}, 
            follow=True
            )

        self.assertTrue(response.context['user'].is_active)
        self.assertEquals(response.status_code, 200)

    def test_loginuser_view_user_is_none(self):
        response = self.client.post(
            '/users/login/', {'username': 'none', 'password': 'none'})

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_loginuser_view_get_method(self):
        response = self.client.get('/users/login/')

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_logoutuser_view(self):
        response = self.client.post(self.logoutuser_url)

        self.assertRedirects(response, reverse('home'))

    def test_moncompte_view(self):
        response = self.client.get(self.moncompte_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/moncompte.html')

    def test_myproducts_view(self):
        response = self.client.get(self.myproducts_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/myproducts.html')

    def test_myproducts_delete_view(self):
        response = self.client.get(self.myproducts_delete_url)

        self.assertEquals(response.status_code, 302)

    # Testing Password Reset Part
    def test_password_reset_view(self):
        response = self.client.get(self.password_reset_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/password/password_reset.html')

    def test_password_reset_view_is_done(self):
        response = self.client.post('users/password_reset/', )
        print(response)

        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(response, 'users/password/password_reset_done')
