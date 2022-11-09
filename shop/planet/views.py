from django.shortcuts import render
from planet.models import Planet, Trip

def menu_view(request):
    queryset = Planet.objects.all()

    return render(request, 'block_content/menu_list.html', {"queryset":queryset})


def trip_view(request):
    queryset = Trip.objects.all()

    return render(request, 'block_content/trips.html', {"queryset":queryset})