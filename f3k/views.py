from django.shortcuts import render
from django.http import HttpResponse
from .models import Utenti


# Create your views here.
def index(request):
    testo = "Applicazione F3K !!!"
    lista_utenti = Utenti.objects.all()
    context={'lista_utenti':lista_utenti}
    return render(request,'f3k/index.html',context)


