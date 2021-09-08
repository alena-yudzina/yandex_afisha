from django.db import models


class Place(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название'
        )
    description_short = models.TextField(
        blank=True,
        verbose_name='Короткое описание'
        )
    description_long = models.TextField(
        blank=True,
        verbose_name='Длинное описание'
        )
    coordinates_lng = models.DecimalField(
        null=True,
        max_digits=16,
        decimal_places=14,
        verbose_name='Долгота'
        )
    coordinates_lat = models.DecimalField(
        null=True,
        max_digits=16,
        decimal_places=14,
        verbose_name='Широта'
        )


    def __str__(self):
        return f'{self.title}'