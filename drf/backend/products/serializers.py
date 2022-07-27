'''
from dataclasses import field
from django import forms
'''
from rest_framework import serializers
from .models import Product, User

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
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ["id","username","password","user_type"]
    def to_representation(self, instance):
        print("instance00",instance)
        relative_path_dict = super(UserSerializer, self).to_representation(instance)
        print("relative_path_dict",relative_path_dict)
        for k in relative_path_dict.keys():
            if k == 'username':
                relative_path_dict[k] = k+"rrrr123"
        print("relative_path_dict1",relative_path_dict)
        return relative_path_dict
    '''
    def validate(self, data, **kwargs): #驗證 之前
        """
        離場日期 >= 進場日期 >= 今天日期。
        """
        data['username'] += 'ssssss'
        return data
        # if data['enter_date'] < datetime.datetime.today().date() or data['leave_date'] < data['enter_date']:
        #     raise serializers.ValidationError(FailApplicationEnterOrLeaveDate)
        # return data
    '''