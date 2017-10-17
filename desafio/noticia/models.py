from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    def __str__(self):
        return self.nome

@python_2_unicode_compatible 
class Noticia(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    titulo = models.CharField(max_length=30)
    texto = models.TextField()
    def __str__(self):
        return self.titulo
    
    
# Create your models here.
