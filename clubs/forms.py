from django import forms
from .models import Club, Personal_Trainer, City_or_Town


class ClubForm(forms.ModelForm):

    class Meta:
        model = Club
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__('args, **kwargs')
        cities_or_towns = City_or_Town.objects.all()
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

