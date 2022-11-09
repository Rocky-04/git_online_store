# Generated by Django 4.1.1 on 2022-10-27 08:34

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ('orders', '0008_goodsintheorder_color_goodsintheorder_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmethod',
            name='title_en',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='title_uk',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='status',
            name='title_en',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='status',
            name='title_uk',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]
