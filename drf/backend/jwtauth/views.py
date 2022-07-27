from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import response, decorators, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import  ProductSerializer01
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
from django.utils.decorators import method_decorator

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

class ProuductMixinView01(mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    queryset=models.Product.objects.all()
    serializer_class = ProductSerializer01
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


class ProuductMixinView01(mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    queryset=models.Product.objects.all()
    serializer_class = ProductSerializer01
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

class ProuductMixinView02(ModelViewSet):
    queryset=models.Product.objects.all()
    serializer_class = ProductSerializer01
    lookup_field='pk'
    authentication_classes=[MyJWTAuthentication,]
    #permission_classes= (AllowAny,)
    permission_classes = [My_Permission,]
    def list(self,request,*args,**kwargs):
        serializer=ProductSerializer01(self.queryset,many=True)
        print("self.queryset",self.queryset)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self,request,*args,**kwargs):
        instance = self.get_object()
        print("instanceinstance",instance)
        serializer = self.get_serializer(instance)
        #serializer=ProductSerializer01(self.queryset,many=True)
        #print("self.queryset",self.queryset)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
