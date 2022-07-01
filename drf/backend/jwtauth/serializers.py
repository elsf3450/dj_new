from django.contrib.auth import get_user_model
from rest_framework import serializers, exceptions
from products import models
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from products.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'username'
    def validate(self,attrs):
        print("attrs",attrs)
        authentication_kwargs={self.username_field:attrs[self.username_field],'password':attrs['password']}
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

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Product
        fields= ["id","title","content", "price","sale_price", "get_discount"]


