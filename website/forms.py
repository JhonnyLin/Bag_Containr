from django import forms
from website.models import Contato

class Mensagem(forms.ModelForm):
    class Meta:
        model = Contato
        fields = [
            'nome',
            'email',
            'assunto',
            'messagem',
        ]