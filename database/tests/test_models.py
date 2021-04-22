from django.test import TestCase

from database.models import Product, Nutriscore


class AuthorModelTest(TestCase):

    def setUp(self):
        nutriscore = Nutriscore.objects.create(nut_id=1, nut_type="C")
        self.product = Product.objects.create(
            prod_id=3017620422003,
            prod_name="test product",
            nut_id=nutriscore,
        )

    def test_first_name_label_and_max_length(self):
        '''
        I test if the nama label and the max length are correct
        '''
        product = Product.objects.get(prod_id=3017620422003)

        field_label = product._meta.get_field('prod_name').verbose_name
        max_length = product._meta.get_field('prod_name').max_length

        self.assertEquals(field_label, 'prod name')
        self.assertEquals(max_length, 250)
