from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import response, decorators, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import  ProductSerializer
from products import models
from rest_framework.response import Response
# Create your views here.
from rest_framework import generics ,mixins,permissions,status
from rest_framework.viewsets import ModelViewSet
from .authentication import MyJWTAuthentication
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import  TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
import uuid
from .permissions import My_Permission
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer

class RefreshView(TokenRefreshView):
    #authentication_classes=[MyJWTAuthentication,]
    #permission_classes= (AllowAny,)
    def post(self, request, *args, **kwargs):
        print("FFFF")
        print("request",request.data)
        #print(super(TokenRefreshView, self).post(request, *args, **kwargs))
        return super(TokenRefreshView, self).post(request, *args, **kwargs)


class ProuductMixinView(mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    queryset=models.Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field='pk'
    authentication_classes=[MyJWTAuthentication,]
    #permission_classes= (AllowAny,)
    permission_classes = [My_Permission,]

    #permission_classes=[My_Permission,]
    #permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    #permission_classes = (IsAuthenticated,)
    #permission_classes=[permissions.DjangoModelPermissions]
    
    def get(self,request,*args,**kwargs):

        pk = kwargs.get("pk")
        print("request.user",request.user)
        print("request11",request)
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        else:
            return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        print("requestrequestrequest30",request.data)
        #return self.list(request,*args,**kwargs)
        request.data['price']=request.data['price']+1000
        
        return self.create(request, *args, **kwargs)

