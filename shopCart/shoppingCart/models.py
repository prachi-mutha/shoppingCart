from django.db import models

# Create your models here.
class Product(models.Model):
	product_name=models.CharField(max_length=50)
	category=models.CharField(max_length=50,default="")
	price=models.IntegerField(default=0)

	desc=models.CharField(max_length=300)
	pub_date=models.DateField()
	image=models.ImageField(upload_to="shoppingCart/static",default="")
	#after creating model now register this in admin.py
	def __str__(self):
		return str(self.id) +' '+ self.product_name 

class Contact(models.Model):
	msg_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	email=models.CharField(max_length=50,default="")
	phone=models.CharField(max_length=70,default="")
	desc=models.CharField(max_length=300)


	def __str__(self):
		return self.name

class Orders(models.Model):
	order_id=models.AutoField(primary_key=True)
	items=models.CharField(max_length=500)
	name=models.CharField(max_length=500)
	email=models.CharField(max_length=500)
	address=models.CharField(max_length=500)
	city=models.CharField(max_length=500)
	zipcode=models.CharField(max_length=500)
	state=models.CharField(max_length=500)
	phone=models.CharField(max_length=200)
	amount=models.IntegerField()

	def __str__(self):
		return str(self.order_id)

class Track(models.Model):
	ordered_id=models.IntegerField(primary_key=True)
	email=models.CharField(max_length=200)
	status=models.CharField(max_length=400)

	def __str__(self):
		return str(self.ordered_id)+' '+self.status