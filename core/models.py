from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100)
    season = models.CharField(max_length=50)
    soil_type = models.CharField(max_length=100)
    sustainability_tips = models.TextField()

    def __str__(self):
        return self.name

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    crops_grown = models.ManyToManyField(Crop)

    def __str__(self):
        return self.name