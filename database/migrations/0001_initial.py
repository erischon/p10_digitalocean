# Generated by Django 3.2 on 2021-05-04 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('cat_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Nutriscore',
            fields=[
                ('nut_id', models.AutoField(primary_key=True, serialize=False)),
                ('nut_type', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('prod_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('prod_name', models.CharField(max_length=250)),
                ('prod_url', models.CharField(max_length=250)),
                ('prod_image', models.CharField(max_length=250, null=True)),
                ('myproduct', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('nut_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.nutriscore')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_id', models.AutoField(primary_key=True, serialize=False)),
                ('shop_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Substitute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oriproduct', to='database.product')),
                ('substitute_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subproduct', to='database.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prodshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.product')),
                ('shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.shop')),
            ],
        ),
        migrations.CreateModel(
            name='Prodcat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.categorie')),
                ('prod_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.product')),
            ],
        ),
        migrations.CreateModel(
            name='Prodbrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.brand')),
                ('prod_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.product')),
            ],
        ),
    ]
