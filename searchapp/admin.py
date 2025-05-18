from django.contrib import admin
from .models import Product, Brand, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'category', 'nutrition_facts']
    exclude = ['search_vector']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category) 
admin.site.register(Brand)  