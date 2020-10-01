from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Contact,Orders,Track
from math import ceil
import smtplib
# Create your views here.
def index(req):
	# products=Product.objects.all()
	# print(products)
	# n=len(products)
	# nslide=n//4+ ceil((n/4)-(n//4))
	# params={'n_slide':nslide,'range':range(1,nslide),'product':products}
	allProds = []
	catprods = Product.objects.values('category', 'id')
	cats = {item['category'] for item in catprods}
	for cat in cats:
		prod = Product.objects.filter(category=cat)
		n = len(prod)
		nSlides = n // 4 + ceil((n / 4) - (n // 4))
		allProds.append([prod, range(1, nSlides), nSlides])
		params = {'allProds':allProds}
	    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
	    # allProds = [[products, range(1, nSlides), nSlides],
	    #             [products, range(1, nSlides), nSlides]]
	   
	return render(req,'index.html',params)

def about(req):
	return render(req,'about.html')

def contact(req):
	if req.method=="POST":
		name=req.POST.get('name','')
		email=req.POST.get('email','')
		phone=req.POST.get('phone','')
		desc=req.POST.get('query','')
		contact=Contact(name=name,email=email,phone=phone,desc=desc)
		contact.save()
	return render(req,'contact.html')

def tracker(req):
	if req.method=="POST":
		email=req.POST.get('email','')
		orderid=req.POST.get('orderid','')
		tracker=Track.objects.filter(ordered_id=orderid)
		trackStatus=tracker[0].status
		return render(req,'tracker.html',{'trackStatus':trackStatus})
	return render(req,'tracker.html')

def search(req):
	if req.method=="GET":
		params=dict()
		lis=[]
		search=req.GET.get('search','')
		#lis=search.split(' ')
		prod = Product.objects.filter(category__icontains=search)
		for row in prod:
			params[row.id]=[row.product_name,row.price,row.desc,row.image]
		
	return render(req,'search.html',{'products':prod})


def productview(req,myid):
	product = Product.objects.filter(id=myid)
	return render(req,'productview.html',{'product':product[0]})

def checkout(req):
	return render(req,'checkout.html')

def orders(req):
	if req.method=="POST":
		name=req.POST.get('name','')
		email=req.POST.get('email','')
		phone=req.POST.get('phone','')
		add=req.POST.get('address','')
		city=req.POST.get('city','')
		zip_=req.POST.get('zip','')
		state=req.POST.get('state','')
		item=req.POST.get('item','')
		x=item.split("a")
		products=dict()
		price=int()
		for i in x[:-1]:
			prod=Product.objects.filter(id=i)
			products[prod[0].product_name+str(prod[0].id)]=prod[0].price
			price+=int(prod[0].price)
		order=Orders(items=x[:-1],name=name,email=email,phone=phone,address=add,city=city,zipcode=zip_,state=state,amount=price)
		order.save()
		tracker=Track(ordered_id=order.order_id,email=email,status="Order has been placed")
		tracker.save()
		try:
			server=smtplib.SMTP('smtp.gmail.com',587)
			server.ehlo() #identify comp
			server.starttls() #transport tlayer security
			content=f"Your Order id is {tracker.ordered_id}"
			f=open('shopping/data.txt','r')
			p=f.readline()
			server.login('pracheejain1398@gmail.com',p)
			server.sendmail('pracheejain1398@gmail.com',{tracker.email},content)
			server.close()
		except:
			return render(req,'tracker.html',{'track':"Your Order Has Been Placed"})
	return render(req,'tracker.html',{'track':"Your Order Has Been Placed"})


	
