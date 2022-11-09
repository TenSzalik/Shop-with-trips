from django.contrib import admin
from .models import Planet, Trip

planet_models = [
    Planet,
    Trip,
]

admin.site.register(planet_models)
