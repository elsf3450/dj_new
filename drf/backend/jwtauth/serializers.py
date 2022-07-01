from django.contrib.auth import get_user_model
from rest_framework import serializers
from products import models
User = get_user_model()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Product
        fields= ["id","title","content", "price","sale_price", "get_discount"]