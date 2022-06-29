from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Products
from django.urls import reverse

# Create your views here.

def index(request):
    products = Products.objects.all().values()
    print(products)
    template = loader.get_template('products.html')
    context = {
        'products': products
    }
    return HttpResponse(template.render(context, request))

def add(request):
    templates = loader.get_template("product-add.html")
    return HttpResponse(templates.render({}, request))

def addrecord(request):
    name = request.POST['name']
    price = int(request.POST['price'])
    product = Products(name=name, price=price)
    product.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    product = Products.objects.get(id=id)
    product.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    product = Products.objects.get(id=id)
    templates = loader.get_template('product-update.html')
    context = {
        'product': product
    }
    return HttpResponse(templates.render(context, request))

def updaterecord(request, id):
    name = request.POST['name']
    price = int(request.POST['price'])
    product = Products.objects.get(id=id)
    product.name = name
    product.price = price
    product.save()
    return HttpResponseRedirect(reverse('index'))
    