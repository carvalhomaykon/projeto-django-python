from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
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
        'site_title': 'Contatos - ',
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

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': site_title,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )

def search(request):
    # contacts = Contact.objects.all() --> Serve para mostrar tudo, mas não queremos mostrar tudo
    search_value = request.GET.get('q', '').strip()
    # strip --> Remove os espaços do começo e do fim
    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects\
        .filter(show=True)\
        .filter(
                # | == or
                Q(first_name__icontains=search_value) | 
                Q(last_name__icontains=search_value) |
                Q(phone__icontains=search_value) |
                Q(email__icontains=search_value)
            )\
        .order_by('-id')[:10]
    
    print(contacts.query)

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - ',
    }

    return render(
        request,
        'contact/index.html',
        context
    )