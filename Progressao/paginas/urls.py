from django.urls import path
from .views import IndexView, BasicModelView, AboutView, InitialView

urlpatterns = [
    #Estrutura básica
    # path('endereço a partir do diretório base/', minhaview.as_view(), name='nome para a url'),
    path('', IndexView.as_view(), name='index'),
    path('inicio/', InitialView.as_view(), name='inicio'),
    path('base/', BasicModelView.as_view(), name='base'),
    path('sobre/', AboutView.as_view(), name='sobre'),
]