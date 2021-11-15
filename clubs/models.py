from django.db import models
import uuid


# Create your models here.
class Club(models.Model):
    club = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=14, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    postcode = models.CharField(max_length=20,  null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address = models.CharField(max_length=80, null=False, blank=False)
    club_opening_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.club
