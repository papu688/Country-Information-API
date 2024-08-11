from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    capital = models.CharField(max_length=100)
    population = models.PositiveIntegerField()
    area = models.FloatField()
    official_languages = models.TextField()
    continent = models.CharField(max_length=100)
    major_cities = models.TextField()
    climate = models.TextField()
    gdp = models.FloatField()
    currency = models.CharField(max_length=100)

    def __str__(self):
        return self.name
