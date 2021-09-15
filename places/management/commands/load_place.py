import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Image, Place


class Command(BaseCommand):
    help = 'Load place to website'

    def add_arguments(self, parser):
        parser.add_argument('json-description', type=str)

    def handle(self, *args, **options):
        response = requests.get(options['json-description'])
        response.raise_for_status()
        place_description = response.json()
        place_json = ContentFile(response.content)
        place, created = Place.objects.get_or_create(
            title=place_description['title'],
            short_title=place_description['title'],
            description_short=place_description['description_short'],
            description_long=place_description['description_long'],
            coordinates_lng=place_description['coordinates']['lng'],
            coordinates_lat=place_description['coordinates']['lat'],
        )
        place.details.save(response.url, place_json, save=True)
        for position, img_link in enumerate(place_description['imgs']):
            image, created = Image.objects.get_or_create(
                place=place,
                position=position,
            )
            img = requests.get(img_link)
            response.raise_for_status()
            f = ContentFile(img.content)
            image.photo.save(img.url, f, save=True)
