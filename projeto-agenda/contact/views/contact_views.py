from django.shortcuts import render, get_object_or_404
from contact.models import Contact
from django.http import Http404

# Create your views here.
def index(request):
    # contacts = Contact.objects.all() --> Serve para mostrar tudo, mas não queremos mostrar tudo
    contacts = Contact.objects\
        .filter(show=True)\
        .order_by('-id')[:10]
    
    print(contacts.query)

    context = {
        'contacts': contacts,   
    }

    return render(
        request,
        'contact/index.html',
        context
    )

# Create your views here.
def contact(request, contact_id):
    # contacts = Contact.objects.all() --> Serve para mostrar tudo, mas não queremos mostrar tudo
    #single_contact = Contact.objects.filter(pk=contact_id).first()
    # pk = id

    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    #if single_contact is None:
    #    raise Http404

    context = {
        'contact': single_contact,   
    }

    return render(
        request,
        'contact/contact.html',
        context
    )