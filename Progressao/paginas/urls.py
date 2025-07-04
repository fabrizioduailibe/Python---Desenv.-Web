from django.urls import path
from .views import IndexView

urlpatterns = [
    #Estrutura básica
    # path('endereço a partir do diretório base/', minhaview.as_view(), name='nome para a url'),
    path('inicio/', IndexView.as_view(), name='inicio'),
]