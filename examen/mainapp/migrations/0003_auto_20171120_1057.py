# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 10:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustProd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Customer')),
            ],
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.AddField(
            model_name='custprod',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Product'),
        ),
        migrations.AlterUniqueTogether(
            name='custprod',
            unique_together=set([('product', 'customer')]),
        ),
    ]