from django.shortcuts import render
from django.http import HttpResponse
from team.models import Team
from slide.models import Slide
# Create your views here.
def index(request):
    # 获取team表数据
    team = Team.objects.all().order_by('rank')
    slide = Slide.objects.all()
    return render(request, 'index.html', {'team': team,'slide': slide})
