from rest_framework import serializers
from .models import Info


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'