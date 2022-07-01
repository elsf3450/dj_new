from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import rest_framework
from .models import Product, User, UserToken
class AuthLogin(BaseAuthentication):
    def authenticate(self, request):
        #print("PP",request.META)
        print("request",request.headers.get("Authorization"))
        token = request.headers.get("Authorization")
        print("token",token)
        user_token = UserToken.objects.filter(token=token).first()
        print(user_token.user.id)
        print(user_token.user.user_type)
        #print("user_token",user_token.id)
        if user_token:
            # 注意此处返回的对象是返回给request.user
            return user_token.user, ''
        else:
            raise rest_framework.exceptions.AuthenticationFailed("您还没有登录")
            #return AuthenticationFailed({"res":'您还没有登录'})

class AuthLogin(BaseAuthentication):
    def authenticate(self, request):
        #print("PP",request.META)
        print("request",request.headers.get("Authorization"))
        token = request.headers.get("Authorization")
        print("token",token)
        user_token = UserToken.objects.filter(token=token).first()
        print(user_token.user.id)
        print(user_token.user.user_type)
        #print("user_token",user_token.id)
        if user_token:
            # 注意此处返回的对象是返回给request.user
            return user_token.user, ''
        else:
            raise rest_framework.exceptions.AuthenticationFailed("您还没有登录")
            #return AuthenticationFailed({"res":'您还没有登录'})