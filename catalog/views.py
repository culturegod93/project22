from django.shortcuts import render

def home(request):
    """Контроллер для главной страницы"""
    context = {
        'title': 'Главная страница',
        'products': [
            {'name': 'Товар 1', 'price': 1000, 'description': 'Описание товара 1'},
            {'name': 'Товар 2', 'price': 1500, 'description': 'Описание товара 2'},
            {'name': 'Товар 3', 'price': 2000, 'description': 'Описание товара 3'},
        ]
    }
    return render(request, 'catalog/home.html', context)

def contacts(request):
    """Контроллер для страницы контактов"""
    context = {
        'title': 'Контакты',
        'company_info': {
            'name': 'Интернет-магазин',
            'address': 'г. Москва, ул. Примерная, д. 123',
            'phone': '+7 (495) 123-45-67',
            'email': 'info@shop.ru',
            'schedule': 'Пн-Пт: 9:00-18:00',
        }
    }
    return render(request, 'catalog/contacts.html', context)
