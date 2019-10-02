from rest_framework import serializers
from .models import Prod1


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prod1
        fields = '__all__'
