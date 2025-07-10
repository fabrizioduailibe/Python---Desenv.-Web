#from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
	template_name = "index.html"

class InitialView(TemplateView):
	template_name = "inicio.html"
	
class BasicModelView(TemplateView):
	template_name = "modelobase.html"

class AboutView(TemplateView):
	template_name = "sobre.html"