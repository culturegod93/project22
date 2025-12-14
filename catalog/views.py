from django.shortcuts import render


def home(request):
    """Отображение главной страницы"""
    return render(request, 'catalog/home.html')


def contacts(request):
    """Отображение страницы контактов с обработкой формы"""
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Здесь можно сохранить данные в базу или отправить email
        print(f"Получено сообщение от {name} ({email}): {message}")

        # Возвращаем страницу с сообщением об успехе
        return render(request, 'catalog/contacts.html', {'success': True})

    return render(request, 'catalog/contacts.html')
