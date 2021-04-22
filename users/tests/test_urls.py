from django.test import SimpleTestCase
from django.urls import reverse, resolve

from users.views import signupuser, moncompte, loginuser, logoutuser, myproducts, myproducts_delete


class UsersTestUrls(SimpleTestCase):

    def test_signup_url_is_resolved(self):
        url = reverse('signupuser')
        self.assertEqual(resolve(url).func, signupuser)

    def test_moncompte_url_is_resolved(self):
        url = reverse('moncompte')
        self.assertEqual(resolve(url).func, moncompte)

    def test_login_url_is_resolved(self):
        url = reverse('loginuser')
        self.assertEqual(resolve(url).func, loginuser)

    def test_logout_url_is_resolved(self):
        url = reverse('logoutuser')
        self.assertEqual(resolve(url).func, logoutuser)

    def test_myproducts_url_is_resolved(self):
        url = reverse('myproducts')
        self.assertEqual(resolve(url).func, myproducts)

    def test_myproducts_delete_url_is_resolved(self):
        url = reverse('myproducts_delete', args=['1'])
        self.assertEqual(resolve(url).func, myproducts_delete)
