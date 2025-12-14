# Интернет-магазин на Django

## Описание проекта
Проект интернет-магазина, разрабатываемый в рамках учебного курса.

## Технологии
- Python 3.11
- asgiref==3.11.0
- Django==5.2.9
- django-bootstrap5==25.3
- sqlparse==0.5.4
- tzdata==2025.3

## Установка
1. Клонировать репозиторий
2. Создать виртуальное окружение: `python -m venv venv`
3. Активировать окружение: `venv\Scripts\activate` (Windows) или `source venv/bin/activate` (Linux/Mac)
4. Установить зависимости: `pip install -r requirements.txt`
5. Выполнить миграции: `python manage.py migrate`
6. Запустить сервер: `python manage.py runserver`

## Структура проекта
- `myshop/` - настройки проекта
- `catalog/` - приложение каталога товаров

## Автор
[Дмитрий Смирнов]
