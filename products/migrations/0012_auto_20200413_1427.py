# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-13 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20200413_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='person_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.MainFilter'),
        ),
    ]