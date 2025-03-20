from django.contrib import admin
from slide.models import Slide

# Register your models here.
class SlideAdmin(admin.ModelAdmin):
  list_display = ('id','title')

admin.site.register(Slide, SlideAdmin)