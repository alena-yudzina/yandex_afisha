from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from places.models import Place


def get_json(request, post_id):
    place_queryset = Place.objects.prefetch_related('images')
    place = get_object_or_404(place_queryset, id=post_id)
    return JsonResponse(
        data={
            'title': place.title,
            'imgs': [image.photo.url for image in place.images.all()],
            'description_short': place.description_short,
            'description_long': place.description_long,
            'coordinates': {
                'lat': place.coordinates_lat,
                'lng': place.coordinates_lng
            }
        },
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 2
        }
    )


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
            "detailsUrl": reverse(get_json, args=[place.id])
          }
        }
        )
    geojson = {
        "type": "FeatureCollection",
        "features": places_description
    }
    return render(request, 'index.html', context={'geojson': geojson})
