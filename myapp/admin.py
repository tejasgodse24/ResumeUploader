from django.contrib import admin
from myapp.models import *
# Register your models here.
@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile_no']

