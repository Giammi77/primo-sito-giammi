from django import forms

class IscrizioneForm(forms,Form):
    Cognome = forms.CharField(label='Cognome',max_length=200)
