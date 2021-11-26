from django.contrib import admin
from .models import Club, Personal_Trainer, City_or_Town


# Register your models here.
class ClubAdmin(admin.ModelAdmin):
    list_display = (
        'club',
        'phone_number',
        'street_address',
        'id',
    )

class PersonalTrainerAdmin(admin.ModelAdmin):
    list_display = (
        'club',
        'full_name',
        'phone_number',
        'image',
    )


admin.site.register(City_or_Town)
admin.site.register(Club, ClubAdmin)
admin.site.register(Personal_Trainer, PersonalTrainerAdmin)
