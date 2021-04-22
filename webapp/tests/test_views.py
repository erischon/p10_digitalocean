from django.test import TestCase, Client
from django.urls import reverse


class WebAppTestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.homepage_url = reverse('home')
        self.mentions_url = reverse('mentions')

    def test_homepage_view(self):
        response = self.client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'webapp/home.html')

    def test_mentions_view(self):
        response = self.client.get(self.mentions_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'webapp/mentions.html')
