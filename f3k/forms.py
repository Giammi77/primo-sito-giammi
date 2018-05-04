from django import forms

class Form_Iscrizione(forms.Form):
    Cognome = forms.CharField(max_length=200)
    Nome = forms.CharField(max_length=200)
