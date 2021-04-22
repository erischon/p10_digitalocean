from django.test import SimpleTestCase
from django.urls import reverse, resolve

from database.views import etl, etl_extract, etl_transform, etl_load, etl_manage_nutriscore, etl_manage_delete


class DatabaseTestUrls(SimpleTestCase):
    '''
    I test all the urls in database app
    '''

    def test_etl_url_is_resolved(self):
        url = reverse('etl')
        self.assertEqual(resolve(url).func, etl)

    def test_etl_extract_url_is_resolved(self):
        url = reverse('etl_extract')
        self.assertEqual(resolve(url).func, etl_extract)

    def test_etl_transform_url_is_resolved(self):
        url = reverse('etl_transform')
        self.assertEqual(resolve(url).func, etl_transform)

    def test_etl_load_url_is_resolved(self):
        url = reverse('etl_load')
        self.assertEqual(resolve(url).func, etl_load)

    def test_etl_manage_nutriscore_url_is_resolved(self):
        url = reverse('etl_manage_nutriscore')
        self.assertEqual(resolve(url).func, etl_manage_nutriscore)

    def test_etl_manage_delete_url_is_resolved(self):
        url = reverse('etl_manage_delete')
        self.assertEqual(resolve(url).func, etl_manage_delete)
