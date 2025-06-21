from django.contrib import admin
import jobs.models as models
from utils.format_rupiah import format_rupiah
from unfold.admin import ModelAdmin

# Register your models here.


@admin.register(models.Job)
class AdminJob(ModelAdmin):
    list_display = ['title', 'get_salary', 'get_company', 'is_remote']

    def get_company(self, obj):
        return f"{obj.company.name}"
    get_company.short_description = 'Company'

    def get_salary(self, obj):
        return format_rupiah(obj.salary)
    get_company.short_description = 'Salary'
