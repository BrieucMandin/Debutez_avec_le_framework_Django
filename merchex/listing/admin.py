from django.contrib import admin
from listing.models import Band, Listings # Importer le modèle Band et Listings
# Register your models here.


class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste

class ListingAdmin(admin.ModelAdmin):  # Ajoute une classe pour Listings (optionnel)
    list_display = ('title', 'band')

admin.site.register(Band,BandAdmin) # nous enregistrons le modèle Band avec l'admin de Django
admin.site.register(Listings, ListingAdmin) # nous enregistrons le modèle Listings avec l'admin de Django

