# Generated by Django 4.1.1 on 2022-10-24 08:51

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0009_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='parent',
            field=models.ForeignKey(blank=True, default=None,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    to='shop.reviews'),
        ),
    ]
