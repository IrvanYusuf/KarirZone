from django.contrib import admin
from companys.models import Company
from unfold.admin import ModelAdmin


@admin.register(Company)
class AdminCompany(ModelAdmin):
    list_display = ['name', 'location', 'employee_count']
