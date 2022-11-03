# Generated by Django 4.1.1 on 2022-10-24 13:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0011_alter_reviews_parent'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reviews',
            unique_together={('user', 'product')},
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='parent',
        ),
    ]
