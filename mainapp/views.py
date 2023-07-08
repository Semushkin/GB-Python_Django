from django.shortcuts import render
import os
import json

# Create your views here.

from mainapp.models import ProductCategories, Product

MODULE_DIR = os.path.dirname(__file__)

'''
def read_file(name):
    file_path = os.path.join(MODULE_DIR, name)
    return json.load(open(file_path, encoding='utf-8'))
'''

def index(request):

    content = {
        'title' : 'Geekshop',
    }
    return render(request, 'mainapp/index.html', content)


def products(request):

    #categories = read_file('fixtures/categories.json')
    #products = read_file('fixtures/goods.json')

    content = {
        'title': 'Geekshop - Каталог',
        'categories': ProductCategories.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, 'mainapp/products.html', content)
