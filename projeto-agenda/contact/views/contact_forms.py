from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from contact.forms import ContactForm
from contact.models import Contact
from django.contrib.auth.decorators import login_required


@login_required(login_url='contact:login')
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

        form = ContactForm(request.POST, request.FILES)

        context = {
            'form': form,
            'form_action': form_action,
        }

        # Salvar o formulário
        if form.is_valid():
            # Quando quiser realizar alguma coisa sem salvar o contato realize:
                #contact = form.save(commit=False)
                #contact.show = False
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
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

@login_required(login_url='contact:login')
def update(request, contact_id):
    # Se eu acessar o site o method ==  GET
    # Se eu enviar o formulário o method == POST
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user
    )

    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        #print ()
        #print (request.method)
        #print (request.POST.get('first_name'))
        #print (request.POST.get('last_name'))
        #print ()

        form = ContactForm(request.POST, request.FILES, instance=contact)

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

@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user
    )
    confirmation = request.POST.get('confirmation', 'no')
    print ('confirmation', confirmation)

    if confirmation == 'yes':
        contact.delete()
        return redirect ('contact:index')
    # Forma simples de deletar contato:
    # contact.delete()
    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation,
        }
    )