# Generated by Django 3.1.4 on 2021-04-20 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_orderdrink_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdrink',
            name='item_price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='orderdrink',
            name='total_price',
            field=models.FloatField(null=True),
        ),
    ]
