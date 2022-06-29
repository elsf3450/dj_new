'''
from dataclasses import field
from django import forms
'''
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields= ["id","title","content", "price","sale_price", "get_discount"]

class ProductSerializer_copy(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields= ["title","content", "price"]

class ProductSerializer_detroy(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields= ["id","title","content", "price","sale_price", "get_discount"]