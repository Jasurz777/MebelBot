# Generated by Django 4.0.6 on 2023-01-10 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg', '0030_remove_product_til'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='til',
            field=models.IntegerField(default=1),
        ),
    ]