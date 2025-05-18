from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()  
    category = serializers.StringRelatedField() 

    class Meta:
        model = Product
        fields = ['name', 'brand', 'category', 'nutrition_facts']