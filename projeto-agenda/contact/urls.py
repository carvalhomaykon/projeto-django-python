from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    # Contact (CRUD)
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'), # Ler o contato
    #path('contact/create/', views.contact, name='contact'), # Criar contato
    #path('contact/<int:contact_id>/update/', views.contact, name='contact'), # Atualizar o contato
    #path('contact/<int:contact_id>/delete/', views.contact, name='contact'), # Deletar o contato
]
