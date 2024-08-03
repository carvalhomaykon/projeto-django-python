from django.shortcuts import render
from contact.forms import ContactForm
from contact.models import Contact

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