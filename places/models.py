from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название'
        )
    short_title = models.CharField(
        max_length=200,
        verbose_name='Короткое название',
        blank=True
        )
    description_short = models.TextField(
        blank=True,
        verbose_name='Короткое описание'
        )
    description_long = HTMLField(
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
    details = models.FileField(
        verbose_name='json-описание',
        null=True,
    )

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название',
        blank=True,
        )
    place = models.ForeignKey(
        Place,
        related_name='images',
        verbose_name='Место',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    photo = models.ImageField(
        verbose_name='Фото',
        null=True,
    )
    position = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name='Позиция',
    )

    class Meta:
        ordering = ['position', ]

    def __str__(self):
        return f'{self.position} {self.name}'
