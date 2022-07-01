from cgitb import lookup
from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework import generics ,mixins,permissions,status
from rest_framework.viewsets import ModelViewSet
from .models import Product ,User ,UserToken
from .serializers import ProductSerializer, ProductSerializer_detroy,UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
import uuid
from .authentication import AuthLogin
from .permissions import My_Permission
'''
class Bill(ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer =ProductSerializer(data=request.data)
        r =serializer.is_valid(raise_exception=False)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
'''
class ProductCreateAPIView_create(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self,serializer):
        print("serializer",serializer.validated_data)
        #title=serializer.validated_data.get("title")
        #content=serializer.validated_data.get("content")
        price=serializer.validated_data.get("price")
        #print("type",type(content))
        title=serializer.validated_data.get("title")
        serializer.save(title='807',content='87',)

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer


class ProductListAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    '''
    def product_alt_view(request ,*args, **kwargs):
        method = request.method
    '''
    #lookup_field = 'pk'

    #Product.objects.get(pk='abc')
class ProductUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer_detroy
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        print("instanceinstance",instance.title)
        print(type(instance))
        instance.title=instance.title+"PP"
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        print("request",request.data)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user_type = request.data.get('user_type')
        print("------------------------------------11")
        print("username",username)
        print("password",password)
        user_obj = User.objects.filter(username=username, password=password).first()
        print("user_obj",user_obj)
        if user_obj:
            token = uuid.uuid4() 
            UserToken.objects.update_or_create(defaults={'token': token}, user_id=user_obj.id)
            #token = token.hex()
            return_msg={'msg':'登录成功', 'token':token}
            return Response(return_msg)
        else:
            return_msg={'msg':'登录失敗', 'token':'token'}
            return Response(return_msg)


class UserView_append(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        #username = request.data.get('username')
        #password = request.data.get('password')
        #user_type = request.data.get('user_type')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class ProuductMixinView(mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field='pk'
    
    authentication_classes=[AuthLogin,]
    permission_classes=[My_Permission,]
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
