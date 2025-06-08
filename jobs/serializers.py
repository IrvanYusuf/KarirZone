from rest_framework import serializers
from jobs.models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

    def validate_description(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError(
                "Field description harus berupa string.")
        return value
