from django.contrib import admin

from .models import Team

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
  list_display = ('name','title')
  search_fields = ('name',)

#将Team注册进后台，并用class teamadmin定义行为
admin.site.register(Team, TeamAdmin)