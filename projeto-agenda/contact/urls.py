from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    # Contact (CRUD)
    path('contact/<int:contact_id>/', views.contact, name='contact'), # Ler o contato
    path('contact/create/', views.create, name='create'), # Criar contato
    path('contact/<int:contact_id>/update/', views.update, name='update'), # Atualizar o contato
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'), # Deletar o contato
]
