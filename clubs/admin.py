from django.contrib import admin
from .models import Club


# Register your models here.
class ClubAdmin(admin.ModelAdmin):
    list_display = (
        'club',
        'phone_number',
        'town_or_city',
        'street_address',
        'id',
    )


admin.site.register(Club, ClubAdmin)
