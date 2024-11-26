from django import forms
from .models import Article, Category

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image', 'categori']  # No incluimos 'date', ya que se asigna automáticamente
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la publicación'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenido'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'categori': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Título',
            'content': 'Contenido',
            'image': 'Imagen',
            'categori': 'Categorías',
        }