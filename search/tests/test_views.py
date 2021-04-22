from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User

from database.models import Product, Nutriscore
from search.views import saving


class SearchTestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

        nutriscore = Nutriscore.objects.create(nut_id=1, nut_type="C")
        self.product = Product.objects.create(
            prod_id=3017620422003,
            prod_name="test product",
            nut_id=nutriscore,
        )
        self.user = User.objects.create_user(
            username="my username",
            password="my pasword"
        )

        self.search_result_url = reverse('search_results')
        self.prodinfos_url = reverse('prodinfos', args=[self.product.prod_id])
        self.search_sub_url = reverse('search_sub')
        self.saving_url = reverse('saving', args=[self.product.prod_id])

    def test_search_results(self):
        response = self.client.get(self.search_result_url, {'user_request': "Test product"})

        self.assertEquals(response.status_code, 200)

    def test_search_results_invalid_form(self):
        response = self.client.get(self.search_result_url, {'user_request': ""})

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/results.html')

    def test_prodinfos_view(self):
        response = self.client.get(self.prodinfos_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/prodinfos.html')

    def test_search_sub_view(self):
        response = self.client.get(self.search_sub_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'webapp/home.html')

    def test_saving_view(self):
        request = self.factory.get('/search/result/')
        request.user = self.user

        response = saving(request, self.product.prod_id)

        self.assertEquals(response.status_code, 302)
