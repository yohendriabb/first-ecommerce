from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
	list_display=['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display=['name', 'slug', 'category', 'description', 'price',  'discount_price','stock', 'available', 'created', 'updated']
	list_filter=['available', 'created', 'updated', 'category']
	list_editable=['price',  'discount_price','stock', 'available']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

admin.site.register(OrderProduct)
admin.site.register(Order)