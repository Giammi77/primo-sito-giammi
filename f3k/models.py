from django.db import models

# Create your models here.

class Utenti(models.Model):
    Cognome = models.CharField(max_length=200)
    Nome = models.CharField(max_length=200)
