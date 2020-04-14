# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-13 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20200413_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainfilter',
            name='category',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='person_category',
            field=models.ForeignKey(choices=[('M', 'Men'), ('W', 'Women'), ('K', 'Kids')], null=True, on_delete=django.db.models.deletion.CASCADE, to='products.MainFilter'),
        ),
    ]