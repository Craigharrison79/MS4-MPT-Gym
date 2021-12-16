from django.db import models
import uuid


# Create your models here.
class City_or_Town(models.Model):
    city_or_town = models.CharField(max_length=40, null=False, blank=False)

    def __str__(self):
        return self.city_or_town

class Club(models.Model):
    club = models.CharField(max_length=200)
    city_or_town = models.ForeignKey('City_or_Town', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=14, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    postcode = models.CharField(max_length=20,  null=False, blank=False)
    street_address = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
        return self.club


class Personal_Trainer(models.Model):
    full_name = models.CharField(max_length=200)
    club = models.ForeignKey('Club', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    speciality1 = models.CharField(max_length=60, null=True, blank=True)
    speciality2 = models.CharField(max_length=60, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    social_link_1 = models.CharField(max_length=200, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.full_name
