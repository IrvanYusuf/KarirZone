from rest_framework import serializers


class PaginationSerializer(serializers.Serializer):
    total_items = serializers.IntegerField()
    total_pages = serializers.IntegerField()
    item_per_page = serializers.IntegerField()
    current_page = serializers.IntegerField()
    has_next = serializers.BooleanField()
    has_previous = serializers.BooleanField()


class BaseResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
    errors = serializers.JSONField(allow_null=True)
    data = serializers.JSONField()  # Bisa override di subclass
