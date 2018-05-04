from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Utenti
from .forms import Form_Iscrizione
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(request):
    testo = "Applicazione F3K !!!"
    lista_utenti = Utenti.objects.all()
    context={'lista_utenti':lista_utenti}
    return render(request,'f3k/index.html',context)

def get_Form_Iscrizione(request):
    if request.method == 'POST':
        form = Form_Iscrizione(request.POST)
        if form.is_valid():
            dati = Utenti.objects.filter(Cognome=request.POST['Cognome']).filter(Nome=request.POST['Nome'])
            if len(dati) !=0:
                form=Form_Iscrizione()
                
            else:
                print (dati)
                dati_da_salvare = Utenti(Cognome=request.POST['Cognome'],Nome=request.POST['Nome'])
                dati_da_salvare.save()
                return HttpResponseRedirect('/f3k')
            
    else :
        form=Form_Iscrizione()
        
    return render(request, 'f3k/iscrizione.html',{'form':form})

    

