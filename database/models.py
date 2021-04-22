from django.db import models
from django.contrib.auth.models import User


class Categorie(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=150)


class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=150)


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=150)


class Nutriscore(models.Model):
    nut_id = models.AutoField(primary_key=True)
    nut_type = models.CharField(max_length=1)


class Product(models.Model):
    prod_id = models.BigIntegerField(primary_key=True)
    prod_name = models.CharField(max_length=250)
    prod_url = models.CharField(max_length=250)
    prod_image = models.CharField(max_length=250, null=True)
    nut_id = models.ForeignKey(Nutriscore, on_delete=models.CASCADE)
    myproduct = models.ManyToManyField(User)

    def __str__(self):
        return self.prod_name


class Prodcat(models.Model):
    cat_id = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class Prodshop(models.Model):
    # prodshop_id = models.AutoField(primary_key=True)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class Prodbrand(models.Model):
    # prodbrand_id = models.AutoField(primary_key=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
