# Generated by Django 3.2.5 on 2021-08-14 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL, verbose_name='user id'),
        ),
    ]
