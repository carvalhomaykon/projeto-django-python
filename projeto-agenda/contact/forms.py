from django.core.exceptions import ValidationError
from django import forms
from . import models

# Criar formulário no django:
# Criar a classe
class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder' : 'Escreva aqui',
            }
        ),
        #label='Primeiro Nome'
        # help_text='Texto de ajuda para seu usuário'
        help_text='Texto de ajuda para seu usuário'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #self.fields['first_name'].widget.attrs.update({
        #    'class': 'classe-a classe-b',
        #    'placeholder' : 'Escreva aqui'
        #})

    # forms.Form -> Criar um formulário do zero
    # forms.ModelForm -> Form baseado num modelo
    # Indicar Models
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )
        #widgets = {
        #    'first_name': forms.TextInput(
        #        attrs={
        #            'class': 'classe-a classe-b',
        #            'placeholder' : 'Escreva aqui'
        #        }
        #    )
        #}
        # 'first_name': forms.PasswordInput() --> Usado para colocar *

    def clean(self):
        # cleaned_data = self.cleaned_data
        #print (cleaned_data)
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de Erro',
                code='invalid'
            )
        )
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de Erro 2',
                code='invalid'
            )
        )
        return super().clean()