from django.contrib import admin
from . models import Category, Blog, Comment
from .models import FeaturedCar

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured',)
    
class FeaturedCarAdmin(admin.ModelAdmin):
    list_display = ['model', 'year', 'price_range', 'status', 'is_featured']
    list_filter = ['status', 'is_featured']
    search_fields = ['model', 'year', 'price_range', 'status']
    prepopulated_fields = {'slug': ('model',)}



admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(FeaturedCar, FeaturedCarAdmin)