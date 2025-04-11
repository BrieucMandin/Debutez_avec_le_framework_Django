from django.http import HttpResponse
from django.shortcuts import render
from listing.models import Band
from listing.models import Listings
from listing.forms import ContactUsForm
from listing.forms import CreateAGroup
from listing.forms import BandForm
from django.core.mail import send_mail
from django.shortcuts import redirect 

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


def contact(request):
  
  # ajoutez ces instructions d'impression afin que nous puissions jeter un coup d'oeil à « request.method » et à « request.POST »
  print('La méthode de requête est : ', request.method)
  print('Les données POST sont : ', request.POST)

  if request.method == 'POST':
     # créer une instance de notre formulaire et le remplir avec les données POST
     form = ContactUsForm(request.POST)
     if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
     return redirect('email-sent')
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
  else:
    form = ContactUsForm()  # ajout d’un nouveau formulaire ici

  return render(request,
          'listing/contact.html',
          {'form': form})  # passe ce formulaire au gabarit

def email_sent(request):
    return render(request, 'listing/email-sent.html')

def error_404_view(request, exception):
    return render(request, 'listing/404.html', status=404)

def band_create(request):

    # ajoutez ces instructions d'impression afin que nous puissions jeter un coup d'oeil à « request.method » et à « request.POST »
  print('La méthode de requête est : ', request.method)
  print('Les données POST sont : ', request.POST)

  if request.method == 'POST':
     # créer une instance de notre formulaire et le remplir avec les données POST
     form = CreateAGroup(request.POST, request.FILES)  # Ajout de request.FILES pour l'image
     if form.is_valid():
        band = Band(
            name=form.cleaned_data['name'],
            biography=form.cleaned_data['biography'],
            year_formed=form.cleaned_data['year_formed'],
            genre=form.cleaned_data['genre'],
            official_homepage=form.cleaned_data['official_homepage'],
            active=form.cleaned_data['active'],
        )
        
        # Gestion de l'image si elle est fournie
        if form.cleaned_data['image']:
            band.image = form.cleaned_data['image']
        
        band.save()
        return redirect('band-list')  # Redirection après la création
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
  else:
    form = CreateAGroup()  # ajout d’un nouveau formulaire ici
    return render(request, 'listing/band_create.html',
          {'form': form})
  

def band_create_example(request):
   if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)
        
   else:
        form = BandForm()


   return render(request,'listing/band_create_example.html',{'form': form})




