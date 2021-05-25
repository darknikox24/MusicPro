from .models import Insumos
from rest_framework import serializers

class InsumosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumos
        fields = '__all__'


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)