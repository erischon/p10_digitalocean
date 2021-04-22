from django.test import TestCase, RequestFactory

from search.search import Search
from database.models import Product, Nutriscore, Prodcat, Categorie


class SearchTestClass(TestCase):

    def setUp(self):
        self.search = Search()
        self.factory = RequestFactory()

        nutriscore_a = Nutriscore.objects.create(nut_id=1, nut_type="A")
        nutriscore_c = Nutriscore.objects.create(nut_id=2, nut_type="C")

        self.product1 = Product.objects.create(
            prod_id=3017620422030,
            prod_name="test product1",
            nut_id=nutriscore_c,
        )
        self.product2 = Product.objects.create(
            prod_id=5117620422051,
            prod_name="test product2",
            nut_id=nutriscore_a,
        )

        self.categorie = Categorie.objects.create(
            cat_id=1,
            cat_name="test categorie"
        )
        self.prodcat1 = Prodcat.objects.create(
            cat_id=self.categorie,
            prod_id=self.product1
        )
        self.prodcat2 = Prodcat.objects.create(
            cat_id=self.categorie,
            prod_id=self.product2
        )

        self.substitute = self.search.find_substitute(self.product1)

    def test_find_product(self):
        response1 = self.search.find_product(self.product1.prod_name)
        response2 = self.search.find_product('produit inconnu')

        self.assertEqual(response1, self.product1)
        self.assertQuerysetEqual(response2, Product.objects.none())

    def test_find_substitute(self):
        response = self.search.find_substitute(self.product1)

        self.assertIsInstance(list(response), list)

    def test_result_infos(self):
        response = self.search.result_infos(self.substitute)

        self.assertIsInstance(list(response), list)

    def test_product_infos(self):
        response = self.search.product_infos(self.product1)

        self.assertIsInstance(response, dict)
