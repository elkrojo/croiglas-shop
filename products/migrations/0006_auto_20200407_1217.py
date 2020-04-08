# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-07 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('LABONE', 'Label One'), ('LABTWO', 'Label Two'), ('LABTHR', 'Label Three'), ('LABFOU', 'Label Four'), ('LABFIV', 'Label Five'), ('LABSIX', 'Label Six'), ('LABSEV', 'Label Seven')], default='LABONE', max_length=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]