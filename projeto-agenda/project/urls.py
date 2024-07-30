from django.contrib import admin
from django.urls import path, include
# Importar bibliotecas p/ mostrar a picture importada pelo usuário
from django.conf.urls.static import static
from django.conf import settings # Assim que faz para buscar dados settings da pasta project

urlpatterns = [
    path('', include('contact.urls')),
    path('admin/', admin.site.urls),
]

# Enviar arquivos para o servidor
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)