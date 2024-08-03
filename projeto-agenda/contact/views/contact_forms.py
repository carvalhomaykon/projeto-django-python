from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from contact.forms import ContactForm
from contact.models import Contact

# Create your views here.
def create(request):
    # Se eu acessar o site o method ==  GET
    # Se eu enviar o formulário o method == POST
    form_action = reverse('contact:create')

    if request.method == 'POST':
        #print ()
        #print (request.method)
        #print (request.POST.get('first_name'))
        #print (request.POST.get('last_name'))
        #print ()

        form = ContactForm(request.POST)

        context = {
            'form': form,
            'form_action': form_action,
        }

        # Salvar o formulário
        if form.is_valid():
            # Quando quiser realizar alguma coisa sem salvar o contato realize:
                #contact = form.save(commit=False)
                #contact.show = False
            contact = form.save()
            return redirect ('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context
        )
    
    context = {
        'form': ContactForm(),
        'form_action': form_action,
    }
    
    return render(
            request,
            'contact/create.html',
            context
        )

def update(request, contact_id):
    # Se eu acessar o site o method ==  GET
    # Se eu enviar o formulário o method == POST
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )

    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        #print ()
        #print (request.method)
        #print (request.POST.get('first_name'))
        #print (request.POST.get('last_name'))
        #print ()

        form = ContactForm(request.POST, instance=contact)

        context = {
            'form': form,
            'form_action': form_action,
        }

        # Salvar o formulário
        if form.is_valid():
            # Quando quiser realizar alguma coisa sem salvar o contato realize:
                #contact = form.save(commit=False)
                #contact.show = False
            contact = form.save()
            return redirect ('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context
        )
    
    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }
    
    return render(
            request,
            'contact/create.html',
            context
        )