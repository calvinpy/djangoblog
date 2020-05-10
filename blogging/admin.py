from django.contrib import admin
from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    ordering = ['title']
    inlines = [CategoryInline, ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)
