from django.contrib import admin
from .models import Gsm

# Register your models here.
@admin.register(Gsm)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id','name','latitude','longitude']
