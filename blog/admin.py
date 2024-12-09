from django.contrib import admin
from .models import Ingredient, Category, Post, Comment, Like
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('id', 'title', 'slug', 'created_on')
    search_fields = ['title']
    list_filter = ('created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)
admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Like)