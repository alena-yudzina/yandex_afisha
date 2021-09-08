# Generated by Django 3.2.7 on 2021-09-08 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description_short', models.TextField(blank=True, verbose_name='Короткое описание')),
                ('description_long', models.TextField(blank=True, verbose_name='Длинное описание')),
                ('coordinates_lng', models.DecimalField(decimal_places=14, max_digits=16, null=True, verbose_name='Долгота')),
                ('coordinates_lat', models.DecimalField(decimal_places=14, max_digits=16, null=True, verbose_name='Широта')),
            ],
        ),
    ]