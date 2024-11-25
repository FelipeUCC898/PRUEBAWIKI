from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.TextField(verbose_name='Description', blank=True)
    create_at = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="fecha")
    update_at = models.DateField(auto_now=True, null=True, blank=True, verbose_name="fecha")

    class Meta: 
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return str(self.name)
    

class Comment(models.Model):
    content = RichTextField(verbose_name='Contenido')
    date = models.DateField(null=True, blank=True, verbose_name="fecha")
    categori = models.ManyToManyField(Category, verbose_name='categoria', blank=True)

    class Meta: 
        verbose_name = 'comentario'
        verbose_name_plural = 'comentarios'
    
    def __str__(self):
        return str(self.content)

    

class Article(models.Model):
    users = models.ManyToManyField(User, verbose_name='usuario', blank=True)
    title = models.CharField(max_length=100, verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to='article')
    likes = models.ManyToManyField(
        'Comment', 
        verbose_name='Número de likes', 
        blank=True, 
        related_name='liked_articles'
    )
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Fecha y hora de publicación")
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Fecha y hora de actualización")
    categori = models.ManyToManyField('Category', verbose_name='Categoría', blank=True)
    comment = models.ManyToManyField(
        'Comment', 
        verbose_name='Comentario', 
        blank=True, 
        related_name='article_comments'
    )

    class Meta: 
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
    
    def __str__(self):
        return self.title


class Reactions(models.Model):
    article = models.ManyToManyField(Article, verbose_name='numero de likes', blank=True)
    users = models.ManyToManyField(User, verbose_name='usuario', blank=True)

    class Meta: 
        verbose_name = 'reacion'
        verbose_name_plural = 'reaciones'

        