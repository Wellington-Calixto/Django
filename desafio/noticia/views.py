from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Categoria, Noticia
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'noticia/index.html'
    context_object_name = 'categorias'   
    def get_queryset(self):
        return Categoria.objects.all()

def categoria_view(request, pk):
    template_name = 'noticia/noticia.html'  
    noticias = Noticia.objects.filter( categoria__id=pk)
    categoria = Categoria.objects.get( id=pk )
    return render(request,  'noticia/noticia.html', {'noticias': noticias, 'categoria': categoria})
      
def noticia_view(request, pk):
    templade_name = 'noticia/conteudo.html'
    noticia = Noticia.objects.get(id=pk)
    categoria = Categoria.objects.get(id=pk)
    return render(request, 'noticia/conteudo.html', {'noticia': noticia, 'categoria': categoria})

# Create your views here.
