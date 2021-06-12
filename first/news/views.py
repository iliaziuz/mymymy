from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm

def news(request):
    news = News.objects.all()
    return render(request, 'news/news.html', {'news': news})


def create(request):
    error = ''
    if request.method =='POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Форма была неверной'


    form = NewsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)