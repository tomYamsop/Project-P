from django.shortcuts import render

from products.models import Printer, PrinterCategory

# Create your views here.
#Контролеры == views == функции

def index(request):
    context = {
        'title': 'не сайт а мечта'
        }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'шучу сайт говна)',
        'catigories': PrinterCategory.objects.all(), 
        'printers': Printer.objects.all(), 
        }
    return  render(request, 'products/products.html', context)
