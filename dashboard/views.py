from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

@login_required(login_url='user-login')
def index(request):
    orders=Order.objects.all()
    products=Product.objects.all()
    workers_count =  User.objects.all().count()
    product_count=Product.objects.all().count()
    order_count=Order.objects.all().count()
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.staff=request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form=OrderForm()
    context={
        'orders':orders,
        'form':form,
        'products':products,
        'workers_count':workers_count,
        'product_count':product_count,
        'order_count': order_count,

    }
    return render(request,'dashboard/index.html', context)

@login_required(login_url='user-login')
def staff(request):
    workers=User.objects.all()
    workers_count =  User.objects.all().count()
    product_count=Product.objects.all().count()
    order_count=Order.objects.all().count()
    context = {
        'workers': workers,
        'workers_count':workers_count,
        'product_count':product_count,
        'order_count': order_count,

    }
    return render(request,'dashboard/staff.html', context)



def staff_detail(request, pk):
    worker=User.objects.get(id=pk)
    context={
        'worker':worker,
    }
    return render(request,'dashboard/staff_detail.html', context )


@login_required(login_url='user-login')
def product(request):
    items = Product.objects.all()#using ORM
    #items = Product.objects.raw('SELECT * FROM dashboard_product')#using SQL
    product_count=Product.objects.all().count()
    workers_count =  User.objects.all().count()
    order_count=Order.objects.all().count()

    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name= form.cleaned_data.get('name')#getting the name of the product we're putting in a request for
            messages.success(request, f'{product_name} has been added.')
            return redirect('dashboard-product')
    else:
        form = ProductForm()

    context = {
        'items': items,
        'form': form,
        'product_count':product_count,
        'workers_count':workers_count,
        'order_count':order_count
    }
    return render(request,'dashboard/product.html', context)  



@login_required(login_url='user-login')
def order(request):
    orders=Order.objects.all()
    order_count=Order.objects.all().count()
    workers_count =  User.objects.all().count()
    product_count=Product.objects.all().count()
    context={
        'orders':orders, 
        'order_count':order_count,
        'workers_count':workers_count,
        'product_count':product_count
    }
    return render(request,'dashboard/order.html', context)


def product_delete(request, pk):
    item = Product.objects.get(id=pk) 
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request,'dashboard/product_delete.html')



def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'templates/dashboard/product_update.html', context) 
