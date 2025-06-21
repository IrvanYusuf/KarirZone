from django.contrib import admin
from banners.models import Banner
from django.utils.html import format_html
from unfold.admin import ModelAdmin
# Register your models here.


@admin.register(Banner)
class AdminBanner(ModelAdmin):
    list_display = ['number', 'url', 'image_preview']
    readonly_fields = ['image_preview_detail']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        self._index = {obj.pk: i for i, obj in enumerate(queryset, start=1)}
        return queryset

    def number(self, obj):
        return self._index.get(obj.pk)
    number.short_description = 'No'

    def image_preview(self, obj):
        if obj.url:
            return format_html('<img src="{}" style="max-height: 60px;" />', obj.url.url)
        return "No image uploaded"
    image_preview.short_description = 'Preview Gambar'

    def image_preview_detail(self, obj):
        if obj.url:
            return format_html('<img src="{}" style="max-height: 200px;" />', obj.url.url)
        return "No image uploaded"
    image_preview.short_description = 'Preview Gambar'
