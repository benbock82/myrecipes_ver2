from django.contrib import admin
from .models import Recipe, Comment


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'title', 'description', 'author')
    list_filter = ('author', 'date_created')
    search_fields = ('title', 'description', 'author')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_created_at', 'recipe', 'author', 'content')
    list_filter = ('comment_created_at',)
    search_fields = ('recipe', 'author', 'content')


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment, CommentAdmin)
