# Generated by Django 3.1.7 on 2021-03-19 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20210316_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_image',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
