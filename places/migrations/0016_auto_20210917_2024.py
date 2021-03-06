# Generated by Django 3.2.7 on 2021-09-17 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0015_remove_place_placeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='coordinates_lat',
            field=models.DecimalField(decimal_places=14, max_digits=16, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='coordinates_lng',
            field=models.DecimalField(decimal_places=14, max_digits=16, verbose_name='Долгота'),
        ),
    ]
