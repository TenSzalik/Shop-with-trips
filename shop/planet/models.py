from django.db import models

from shop.models import BaseModel


class Planet(BaseModel):
    name = models.CharField(max_length=32)
    multimedia = models.ImageField(null=True, blank=True)
    description = models.TextField()
    surface_temperature = models.CharField(max_length=32, null=True, blank=True)
    fun_fact = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]

class Trip(BaseModel):
    SLOGANS = {"Unbelievable", "Magic", "Luxury"}

    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    price = models.FloatField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    is_safely = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return str(next(iter(self.SLOGANS)))+" trip on"+f" {self.planet.name}"