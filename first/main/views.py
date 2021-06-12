from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', data)

def about(request):
    data = {
        'about': 'Обо мне'
    }
    return render(request, 'main/about.html', data)

def contacts(request):
    data = {
        'contacts': 'Контакты'
    }
    return render(request, 'main/contacts.html', data)