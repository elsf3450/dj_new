from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken,AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import exceptions

from django.utils.translation import gettext_lazy as _

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
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer

class MyJWTAuthentication(JWTAuthentication):
    def  get_user(self,validated_token):
        try:
            user_id=validated_token['user_id']
        except KeyError:
            raise InvalidToken(_("token contained"))
        try:
            user = User.objects.get(**{'id':user_id})
        except User.DoesNotExist:
            raise AuthenticationFailed(_('USER NOT FOUND'),code='user not found QQ')
        return user