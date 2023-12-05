from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('InputName')
        email = request.POST.get('InputEmail')
        message = request.POST.get('InputMessage')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contacts.html')


def product(request):
    context = {

    }
    return render(request, 'catalog/product.html')
