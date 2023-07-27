from django.contrib import admin
from news.models import Author, Category, Article
from forms import ArticleForm

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    list_display = ('title', 'author', 'category', 'status')