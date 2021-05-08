from django.db import models
from django.conf import settings
from django.shortcuts import reverse

class Category(models.Model):
	name = models.CharField('Name', max_length=200, unique=True, blank=True, db_index=True)
	slug = models.SlugField('Slug',max_length=200, unique=True , blank=False)
	
	def __str__(self):
		return self.name
	
	class Meta:
		ordering= ('name',)
		verbose_name='Category'
		verbose_name_plural='Categories'

	def get_absolute_url(self):
		return reverse("category_display", kwargs={
			'slug': self.slug
		})

class Product(models.Model):
	category= models.ForeignKey(Category, related_name='products' , on_delete=models.CASCADE)
	name = models.CharField('Name', max_length=50)
	slug = models.SlugField('Slug', db_index=True, unique=True)
	image = models.ImageField (upload_to='media/%y/%m/%d', blank=True)
	description = models.TextField('description', blank=True)
	price = models.DecimalField('price', max_digits=200, decimal_places=2)
	discount_price = models.DecimalField('Discount_price', default=0, max_digits=200, decimal_places=2)
	stock = models.PositiveIntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	quantity = models.IntegerField(default=1)

	class Meta:
		ordering= ('-created',)
		index_together = (('id', 'slug'),)
		verbose_name='Product'
		verbose_name_plural='Products'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("product_detail", kwargs={ 
			'slug':	self.slug
		})

	def get_add_to_cart_url(self):
		return reverse("add-to-cart", kwargs={
			'slug': self.slug
		})

	def get_remove_form_cart_url(self):
		return reverse("remove-from-cart", kwargs={
			'slug': self.slug
		})

	
class OrderProduct(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	ordered = models.BooleanField(default=False)
	quantity = models.IntegerField(default=1)

	def __str__(self):
		return f"{self.product.quantity} of {self.product.name}"


class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
	start_date = models.DateTimeField(auto_now_add=True)
	product = models.ManyToManyField(OrderProduct)
	ordered_date = models.DateTimeField()
	ordered = models.BooleanField(default=False)
	quantity = models.IntegerField(default=1)

def __str__(self):
	return f"{self.user.username}"
