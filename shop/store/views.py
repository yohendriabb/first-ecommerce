from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView, DetailView, UpdateView ,DeleteView
from django.utils import timezone
from django.contrib import messages
from .models import *


class CategoryView(View):
	model = Category
	template_name="product/product.html"

class Product_list(ListView):
	model = Product
	template_name= 'core/base.html'

class ProductDetail(DetailView):
	model = Product
	template_name = 'product/product.html'

def add_to_cart(request, slug):
	product = get_object_or_404(Product, slug=slug)
	order_product, created = OrderProduct.objects.get_or_create(product=product)
	order_qs = Order.objects.filter(user=request.user, ordered=False)
	if order_qs.exists():
		order = order_qs[0]

		if order.product.filter(product__slug=product.slug).exists():
			order_product.quantity += 1
			order_product.save()
			messages.info(request, "Producto agregado a su carrito")
			return redirect("product_detail", slug=slug)

		else:
			order.product.add(order_product)
			messages.info(request, "This item was added to your cart.")
			return redirect("product_detail", slug=slug)
	else:
		ordered_date = timezone.now()
		order = Order.objects.create(
			user=request.user, ordered_date=ordered_date)
		order.product.add(order_product)
		messages.info(request, "Este producto a sido agregado a su carrito.")
		return redirect("product_detail", slug=slug)


def remove_from_cart(request, slug):
	Product = get_object_or_404(Product, slug=slug)
	order_qs = Order.objects.filter(
		user=request.user,
		ordered=False
	)
	if order_qs.exists():
		order = order_qs[0]
		# check if the order item is in the order
		if order.product.filter(product__slug=product.slug).exists():
			order_product = OrderProduct.objects.filter(product=product, user=request.user,	ordered=False)[0]
			order_product.remove(order_product)
			order_product.delete()
			messages.info(request, "Este roduvto a sido elimiado del carrito.")
			return redirect("product_detail", slug=slug)
		else:
			messages.info(request, "Este Producto ya no se encuetnra en su carrito")
			return redirect("product_detail", slug=slug)
	else:
		messages.info(request, "Usted no posee una orden activa")
		return redirect("product_detail", slug=slug)