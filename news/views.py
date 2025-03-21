from django.http import HttpResponse
from django.shortcuts import render
from .models import News

# Create your views here.
def news_list(request):
  news_list = News.objects.all()
  return render(request, 'list.html', {'news_list':news_list})

def detail(request, id):
  try:
    news = News.objects.get(pk=id)
    return render(request, 'detail.html',{'news':news} )
  except:
    return render(request, '404.html')

