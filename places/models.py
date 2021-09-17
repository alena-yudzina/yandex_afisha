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
        max_digits=16,
        decimal_places=14,
        verbose_name='Долгота'
        )
    coordinates_lat = models.DecimalField(
        max_digits=16,
        decimal_places=14,
        verbose_name='Широта'
        )
    details = models.FileField(
        verbose_name='json-описание',
        null=True,
    )

    def __str__(self):
        return self.title


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
        on_delete=models.CASCADE,
    )
    photo = models.ImageField(
        verbose_name='Фото',
    )
    position = models.PositiveIntegerField(
        default=0,
        verbose_name='Позиция',
    )

    class Meta:
        ordering = ['position', ]

    def __str__(self):
        return f'{self.position} {self.name}'
