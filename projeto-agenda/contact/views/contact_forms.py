from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.http import Http404
from django.core.paginator import Paginator
from django import forms

# Criar formulário no django:
# Criar a classe
class ContactForm(forms.ModelForm):
    # forms.Form -> Criar um formulário do zero
    # forms.ModelForm -> Form baseado num modelo
    # Indicar Models
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone'
        )


# Create your views here.
def create(request):
    # Se eu acessar o site o method ==  GET
    # Se eu enviar o formulário o method == POST
    if request.method == 'POST':
        #print ()
        #print (request.method)
        #print (request.POST.get('first_name'))
        #print (request.POST.get('last_name'))
        #print ()

        context = {
            'form': ContactForm(request.POST)
        }


        return render(
            request,
            'contact/create.html',
            context
        )
    
    context = {
        'form': ContactForm(data=request.POST)
        }
    
    return render(
            request,
            'contact/create.html',
            context
        )