from django.contrib import admin
from contact import models

@admin.register (models.Contact)
# Register your models here.
class ContactAdmin (admin.ModelAdmin):
    # Configurar admin
    # Colocar quais campos quero ver na admin
    # Traduzindo pra tabela, quai valores quero mostrar por coluna
    list_display = 'id', 'first_name', 'last_name', 'phone', 'show',
    # Ordenar as colunas de acordo com um valor
    ordering =  '-id', # Ordenar em ordem decrescente
                #'id' -->  Ordenar de acordo com id em ordem crescente
    # Filtrar algo
    # list_filter = 'created_date',
    # Criar o campo de pesquisar
    search_fields = 'id', 'first_name', 'last_name',
    # Criar paginação, limites de usuário por página
    list_per_page = 10
    # Lista um número de máximo, caso o usuário click em "mostrar tudo"
    list_max_show_all = 200 # No máx 200
    # Informar quais campo quer que sejam editados
    list_editable = 'first_name', 'last_name', 'show',
    # Criar link de acesso para o cliente
    # Não pode adicionar valores que estão na lista 'list_editable'
    list_display_links =  'id', 'phone',
                
@admin.register (models.Category)
class CategoryAdmin (admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',