from django.db import connection
from database.models import Product, Categorie, Prodcat, Brand, Prodbrand, Shop, Prodshop


class DBManage:

    def __init__(self):
        """ """
        self.connection = connection.cursor()

    def load_nutriscore(self):
        """ I load the nutriscore and their id into the table. """
        try:
            query = "INSERT INTO database_nutriscore (nut_id, nut_type) VALUES (1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E'), (6, 'X')"
            self.connection.execute(query)
            message = "REUSSITE : Les différents Nutriscore ont été chargés dans la base."
            return message

        except Exception as ex:
            return ex

    def delete_tables(self):
        """ I delete the data of all the tables except Nutriscore. """
        Prodshop.objects.all().delete()
        Prodbrand.objects.all().delete()
        Prodcat.objects.all().delete()
        Shop.objects.all().delete()
        Brand.objects.all().delete()
        Categorie.objects.all().delete()
        Product.objects.all().delete()
        return "Les Tables sont effacées."
