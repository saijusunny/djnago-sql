from itertools import product
from unicodedata import name
from django.shortcuts import redirect, render
from .models import ProductDetails

# Create your views here.

#delete page
#def delete(request):
#     return render(request,'delete.html')

#load edit page
def edit(request,pk):
    products=ProductDetails.objects.get(id=pk)
    return render(request,'edit.html', {'products':products})

#home for views
#def view(request):
   # return render(request,'view.html')

#index for form
def form(request):
    return render(request,'form.html')
    

def product_details(request):
    if request.method=="POST":
        pname=request.POST['product_name']
        des=request.POST['description']
        qty=request.POST['product_quantity']
        price=request.POST['product_price']

        result=ProductDetails(product_name=pname,
                            description=des,
                            product_quantity=qty,
                            product_price=price,
                            )
        result.save()
        return redirect('view')

        #show products
def view(request):
    products=ProductDetails.objects.all()
    return render(request,'view.html', {'products':products})


#editing page
def edit_details(request,pk):
    if request.method=='POST':
        products = ProductDetails.objects.get(id,pk)
        products.product_name=request.POST.get('product_name')
        products.description=request.POST.get('description')
        products.product_quantity=request.POST.get('product_quantity')
        products.product_price=request.POST.get('product_price')
        products.save()
        return redirect('view')
    return render(request, 'edit.html')

#delete

def delete(request,pk):
    products=ProductDetails.objects.get(id=pk)
    return render(request,'delete.html', {'products':products})

#deleting products

def delete_product(request,pk):
    products=ProductDetails.objects.get(id=pk)
    products.delete()
    return redirect('view')