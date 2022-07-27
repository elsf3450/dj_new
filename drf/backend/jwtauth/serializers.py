from django.contrib.auth import get_user_model
from rest_framework import serializers, exceptions
from products import models
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from products.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'username'
    def validate(self,attrs):
        print("attrs",attrs)
        authentication_kwargs={"username":attrs["username"],'password':attrs['password']}
        print(authentication_kwargs)
        
        try:
            print("print")
            user=User.objects.filter(**authentication_kwargs).first()
            print("user",user)
        except Exception as e:
            raise exceptions.NotFound(e.args[0])
        refresh = self.get_token(user)
        data={"userid":user.id,"token":str(refresh.access_token),"refresh":str(refresh)}
        print("data",data)
        return data

class ProductSerializer01(serializers.ModelSerializer):
    class Meta:
        model=models.Product
        fields= ["id","title","content", "price","sale_price", "get_discount"]
    def to_representation(self, instance):
        print("instance00",instance)
        relative_path_dict = super(ProductSerializer01, self).to_representation(instance)
        print("relative_path_dict0",relative_path_dict)
        for k in relative_path_dict.keys():
            if k == 'price':
                relative_path_dict[k] = int(float(relative_path_dict[k])) * 10000
        print("relative_path_dict1",relative_path_dict)
        return relative_path_dict

