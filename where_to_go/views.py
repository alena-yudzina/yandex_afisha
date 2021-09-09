from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from places.models import Place


def show_index(request):
    places = Place.objects.all()
    places_description = []
    for place in places:
        places_description.append({
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [place.coordinates_lng, place.coordinates_lat]
          },
          "properties": {
            "title": place.short_title,
            "placeId": place.placeId,
            "detailsUrl": place.detailsUrl
          }
        })
    geojson = {
        "type": "FeatureCollection",
        "features": places_description
    }
    return render(request, 'index.html', context={'geojson': geojson})
