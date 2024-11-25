from django.contrib import admin
from .models import Category, Comment, Article, Reactions


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    search_fields = ('name',)
    list_display = ('name', 'create_at', 'update_at')
    ordering = ('-create_at',)

admin.site.register(Category, CategoryAdmin)


class CommentAdmin(admin.ModelAdmin):
    search_fields = ('content',)
    list_display = ('content', 'date')
    ordering = ('-date',)

admin.site.register(Comment, CommentAdmin)


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('update_at',)
    search_fields = ('title', 'users__username')
    list_display = ('title', 'date', 'update_at')
    list_filter = ('date', 'categori')
    ordering = ('-date',)

admin.site.register(Article, ArticleAdmin)


class ReactionsAdmin(admin.ModelAdmin):
    search_fields = ('article__title', 'users__username')
    list_display = ('id',)  

admin.site.register(Reactions, ReactionsAdmin)