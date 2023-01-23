from django.contrib import admin
from testapp.models import Mymodel

# Register your models here.
class Myadmin(admin.ModelAdmin):
    list_display=['name','role','project','location','email']
admin.site.register(Mymodel,Myadmin)
