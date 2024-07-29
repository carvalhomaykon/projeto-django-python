from django.db import models
from django.utils import timezone

# id (primary key - automático)
# Create your models here.
# first_name (string), last_name (string), phone (string)
# emial (email), created_date (date), description (text)
# category (foreing key), show (boolean), owner (foreing key)
# picture (image)

# É melhor trabalhar com palavras singulares
class Contact(models.Model): # Criação da tabela
    # Criação dos campos
    first_name = models.CharField(max_length=50) # Max lenght (Máximo de letras)
    last_name = models.CharField(max_length=50)
    phone = models.CharField (max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    # blank = true --> Deixa opcional, se não é obrigatório inserir aquele elemento
    created_date = models.DateTimeField(default=timezone.now)
    # default=timezone.now --> Faz com que o usuário não inseri a data e sim o django automaticamente inserir a data atual
    description = models.TextField(blank=True) # Por ser Text, não é obrigatório colocar o limitador de caracteres

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
