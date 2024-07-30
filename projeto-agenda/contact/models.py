from django.db import models
from django.utils import timezone

# id (primary key - automático)
# Create your models here.
# first_name (string), last_name (string), phone (string)
# emial (email), created_date (date), description (text)
# category (foreing key), show (boolean), picture (image)
# owner (foreing key)

# Chave estrangeira
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'

# É melhor trabalhar com palavras singulares
class Contact(models.Model): # Criação da tabela / model
    # Criação dos campos
    first_name = models.CharField(max_length=50) # Max lenght (Máximo de letras)
    last_name = models.CharField(max_length=50)
    phone = models.CharField (max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    # blank = true --> Deixa opcional, se não é obrigatório inserir aquele elemento
    created_date = models.DateTimeField(default=timezone.now)
    # default=timezone.now --> Faz com que o usuário não inseri a data e sim o django automaticamente inserir a data atual
    description = models.TextField(blank=True) # Por ser Text, não é obrigatório colocar o limitador de caracteres
    # Campo para saber se quero ou não exibir aquele contato
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/') # upload_to --> Pra qual pasta enviar
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    # on_delete --> Devido está linkando outro model, tenho que informar que quandor apagar a category, o que fazer com o contato?
        # models.CASCADE --> Todos os contatos da categoria serão excluidos
        # models.SET_NULL --> quandoo excluido o campo category vai ser nulo

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
