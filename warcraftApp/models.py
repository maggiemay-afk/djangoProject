from django.db import models


# Create your models here.
class SurveyModel(models.Model):
    character_name = models.CharField(max_length=100)
    fav_zone = models.CharField(max_length=100)
    image_description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='warcraftApp/files/covers')


