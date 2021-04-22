from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from database.models import Nutriscore


class DatabaseTestViews(TestCase):
    '''
    I test all the views in database app
    '''

    def setUp(self):
        self.client = Client()
        Nutriscore.objects.create(nut_id=1, nut_type="C")

        self.credentials_admin = {
            'username': 'admin',
            'password': 'secret',
            'is_staff': True,
        }
        User.objects.create_user(**self.credentials_admin)

        self.credentials_user = {
            'username': 'testuser',
            'password': 'secret',
        }
        User.objects.create_user(**self.credentials_user)

        self.admin_user = User.objects.get(username='admin')
        self.user = User.objects.get(username='testuser')

        self.etl_url = reverse('etl')
        self.etl_extract_url = reverse('etl_extract')
        self.etl_transform_url = reverse('etl_transform')
        self.etl_load_url = reverse('etl_load')

    # === Test Method etl ===

    def test_etl_view_user_not_logged(self):
        response = self.client.get(self.etl_url)

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/users/login/?next=/database/')

    def test_etl_view_user_logged(self):
        self.client.login(**self.credentials_user)

        response = self.client.get(self.etl_url)

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/users/login/?next=/database/')

    def test_etl_view_is_staff(self):
        self.client.login(**self.credentials_admin)

        response = self.client.get(self.etl_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'database/etl.html')

    # def test_etl_extract_view(self):
        # self.client.login(**self.credentials_admin)

        # response = self.client.get(self.etl_extract_url)

        # self.assertEquals(response.status_code, 200)
        # self.assertTemplateUsed(response, 'database/etl.html')

    # def test_etl_transform_view(self):
    #     self.client.login(**self.credentials_admin)

    #     response = self.client.get(self.etl_transform_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'database/etl.html')

    # def test_etl_extract_load_view(self):
        # self.client.login(**self.credentials_admin)

        # response = self.client.get(self.etl_load_url)

        # self.assertEquals(response.status_code, 200)
        # self.assertTemplateUsed(response, 'database/etl.html')
