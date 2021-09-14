# Generated by Django 3.2.7 on 2021-09-14 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_auto_20210910_1845'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='image',
            name='position',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
