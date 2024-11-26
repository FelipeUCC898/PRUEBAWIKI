from django.shortcuts import render, redirect
from .models import Category, Article
from django.contrib import messages
from .forms import ArticleForm
from .models import Category, Comment, Article, Reactions

# Vista para mostrar publicaciones
def publicacion(request):
    category = Category.objects.all()
    comment = Comment.objects.all()
    article = Article.objects.all().order_by('-date')  # Orden ascendente: más viejas primero
    reactions = Reactions.objects.all()

    return render(request, 'blogs/publicacion.html', {
        'titles': 'publicacion',
        'categorys': category,
        'comments': comment,
        'articles': article,
        'reactions': reactions,
    })
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()  # Guarda el artículo
            form.save_m2m()  # Guarda relaciones ManyToMany (como categorías)
            messages.success(request, '¡Artículo creado con éxito!')
            return redirect('publicacion')  # Redirige a la vista principal
    else:
        form = ArticleForm()

    return render(request, 'blogs/create_article.html', {
        'form': form,
        'title': 'Crear Publicación',
    })