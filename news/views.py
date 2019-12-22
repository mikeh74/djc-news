from django.shortcuts import get_object_or_404, render

from .models import News

def index(request):
    news_list = News.objects.order_by('-pub_date')[:9]
    context = {'news_list': news_list}
    return render(request, 'news/index.html', context)

def detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    return render(request, 'news/detail.html', {'news': news})
