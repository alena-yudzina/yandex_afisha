from django.conf import settings
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from places.models import Place
import json


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


def show_place(request, post_id):
    place = get_object_or_404(Place, id=post_id)
    with open(str(place.details.file)) as f:
      place_details = f.read()
    return JsonResponse(
      json.loads(place_details),
      safe=False,
      json_dumps_params={'ensure_ascii': False, 'indent': 2}
      )
