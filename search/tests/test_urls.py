from django.test import SimpleTestCase
from django.urls import reverse, resolve

from search.views import search_sub, search_results, prodinfos, saving


class SearchTestUrls(SimpleTestCase):

    def test_search_sub_url_is_resolved(self):
        url = reverse('search_sub')
        self.assertEqual(resolve(url).func, search_sub)

    def test_search_results_url_is_resolved(self):
        url = reverse('search_results')
        self.assertEqual(resolve(url).func, search_results)

    def test_prodinfos_url_is_resolved(self):
        url = reverse('prodinfos', args=['1'])
        self.assertEqual(resolve(url).func, prodinfos)

    def test_saving_url_is_resolved(self):
        url = reverse('saving', args=['1'])
        self.assertEqual(resolve(url).func, saving)
