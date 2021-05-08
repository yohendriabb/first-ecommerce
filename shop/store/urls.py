from django.urls import path
from .views import *
urlpatterns= [
	path('',  Product_list.as_view(), name="product_list"),
	path('product/<slug>/', ProductDetail.as_view(), name="product_detail"),
	path('category/<slug>/', CategoryView.as_view(), name="category_display"),

	path('add-to-cart/<slug>/', add_to_cart, name="add-to-cart"),
	path('remove-from-cart/<slug>/', remove_from_cart, name="remove-from-cart"),
	

]