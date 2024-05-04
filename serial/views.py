from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Serial_Name, Get_Actior
# Create your views here.


def get_info(request):
    categories = Serial_Name.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)

def get_products(request, pk):
    products = Get_Actior.objects.filter(serial=pk)
    context = {
        'products': products
    }
    return render(request, 'products.html', context=context)

def detail(request, pk):
    product = Get_Actior.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'detail.html', context=context)

def add_products(request):
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('products:get_info')
    context = {
        'form': form
        }
    return render(request, 'create.html', context=context)


def update_products(request, pk):
    data = Get_Actior.objects.get(pk=pk)
    form = ProductForm(request.POST, request.FILES, instance=data)
    if form.is_valid():
        print(1)
        form.save()
        return redirect('products:get_info')
    context = {
        'form': form
        }
    return render(request, 'update.html', context=context)




from django.shortcuts import get_object_or_404

def delete_product(request, pk):
    product = get_object_or_404(Get_Actior, pk=pk)
    
    if request.method == 'POST':
        product.delete()
        return redirect('products:get_info')
    
    return render(request, 'delete.html', {'product': product})



