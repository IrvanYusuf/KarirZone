from django.contrib import admin
from companys.models import Company


@admin.register(Company)
class AdminCompany(admin.ModelAdmin):
    list_display = ['name', 'location', 'employee_count']
