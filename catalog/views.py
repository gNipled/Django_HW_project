from django.shortcuts import render
from catalog.models import Product, Category


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('InputName')
        email = request.POST.get('InputEmail')
        message = request.POST.get('InputMessage')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contacts.html')


def product(request, pk):
    context = {
        'object': Product.objects.get(pk=pk)
    }
    return render(request, 'catalog/product.html', context)
