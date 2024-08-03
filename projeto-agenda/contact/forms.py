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
            'email', 'description', 'category',
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
        cleaned_data = self.cleaned_data
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                    'Primeiro nome não pode ser igual ao segundo',
                    code='invalid'
                )
            self.add_error ('first_name', msg)
            self.add_error ('last_name', msg)

        return super().clean()


        #print (cleaned_data)
        # Para validação de usa o clean
        #self.add_error(
        #    'first_name',
        #    ValidationError(
        #        'Mensagem de Erro',
        #        code='invalid'
        #    )
        #)
        #self.add_error(
        #    'first_name',
        #    ValidationError(
        #        'Mensagem de Erro 2',
        #        code='invalid'
        #    )
        #)
        # add_error -> Pega todos os erros dos campos
        # raise -> Pega o primeiro error e para a execução do código.
        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if first_name == 'ABC':
            self.add_error (
                'first_name',
                ValidationError(
                'Não digite ABC nesse campo',
                code='invalid'
                )
            )

        return first_name