from django.shortcuts import render
from django.http import HttpResponse
from team.models import Team
# Create your views here.
def index(request):
    # 获取team表数据
    team = Team.objects.all().order_by('rank')
    return render(request, 'index.html',{'team': team},)
