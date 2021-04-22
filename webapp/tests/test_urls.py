from django.test import SimpleTestCase
from django.urls import reverse, resolve

from webapp.views import home_page, mentions


class WebappTestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home_page)

    def test_mentions_url_is_resolved(self):
        url = reverse('mentions')
        self.assertEqual(resolve(url).func, mentions)
