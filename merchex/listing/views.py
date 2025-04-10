from django.http import HttpResponse
from django.shortcuts import render
from listing.models import Band
from listing.models import Listings

# Create your views here.

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listing/hello.html', {'bands': bands})

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    listings = Listings.objects.all()
    return render(request, 'listing/listings.html', {'listings': listings})

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listing/band_list.html', {'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listing/band_detail.html', {'band': band,
                                                        'id':id})







