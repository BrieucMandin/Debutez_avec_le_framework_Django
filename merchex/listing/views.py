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





