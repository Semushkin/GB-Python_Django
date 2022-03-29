from django.shortcuts import render

# Create your views here.


def index(request):

    prod = [
        {'name': 'Худи черного цвета с монограммами adidas Originals',
         'pictures': 'vendor/img/products/Adidas-hoodie.png',
         'price': '6 090,00 руб.',
         'text': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'}
    ]

    content = {
        'title' : 'Geekshop',
    }
    return render(request, 'mainapp/index.html', content)


def products(request):

    categories = [{
        'name' : 'Новинки'},
        {'name': 'Одежда'},
        {'name': 'Обувь'},
        {'name': 'Аксессуары'},
        {'name': 'Подарки'},
    ]

    prods = [
        {'name' : 'Худи черного цвета с монограммами adidas Originals',
         'pictures': 'vendor/img/products/Adidas-hoodie.png',
         'price': '6 090,00 руб.',
         'text': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},

        {'name': 'Синяя куртка The North Face',
         'pictures': 'vendor/img/products/Blue-jacket-The-North-Face.png',
         'price': '23 725,00 руб.',
         'text': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},

        {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
         'pictures': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
         'price': '3 390,00 руб.',
         'text': 'Материал с плюшевой текстурой. Удобный и мягкий.'},

        {'name': 'Черный рюкзак Nike Heritage',
         'pictures': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
         'price': '2 340,00 руб.',
         'text': 'Плотная ткань. Легкий материал.'},

        {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
         'pictures': 'vendor/img/products/Black-Dr-Martens-shoes.png',
         'price': '13 590,00 руб.',
         'text': 'Гладкий кожаный верх. Натуральный материал.'},

        {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
         'pictures': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
         'price': '2 890,00 руб.',
         'text': 'Легкая эластичная ткань сирсакер Фактурная ткань.'}
    ]

    content = {
        'title' : 'Geekshop - Каталог',
        'categories': categories,
        'prods': prods
    }
    return render(request, 'mainapp/products.html', content)
