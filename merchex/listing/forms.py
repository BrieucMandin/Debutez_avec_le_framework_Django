# listings/forms.py

from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Band  



class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)

class CreateAGroup(forms.Form):
    name = forms.CharField(max_length=100, label="Nom du groupe")
    biography = forms.CharField(
        max_length=1000, widget=forms.Textarea, label="Biographie"
    )
    year_formed = forms.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2025)],
        label="Année de formation"
    )
    genre = forms.ChoiceField(choices=Band.Genre.choices, label="Genre musical")
    official_homepage = forms.URLField(required=False, label="Site officiel")
    active = forms.BooleanField(initial=True, required=False, label="Actif")
    image = forms.ImageField(required=False, label="Image")

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'
        widgets = {
            'biography': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }




def band_create(request):
   form = BandForm()
   return render(request,
            'listings/band_create.html',
            {'form': form})