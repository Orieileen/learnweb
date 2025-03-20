from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def news_list(request):
  
  return render(request, 'list.html')

def detail(request, id):
  return render(request, 'detail.html')