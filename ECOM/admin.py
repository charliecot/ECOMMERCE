from django.contrib import admin

# Register your models here.

from .models import Category  , Product


class CategoryAdmin(admin.ModelAdmin):
    
    
    fields=['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):

    list_display = ['title','author','slug',
    'price','in_stock','created','updated']
    list_filter = ['in_stock','is_active']
    list_edit=['price','in_stock']
    prepopulated_fields = { 'slug' : ('title',)}

admin.site.register(Product, ProductAdmin)

