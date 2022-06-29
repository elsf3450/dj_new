from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework import generics ,mixins
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer, ProductSerializer_detroy
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
        serializer.save(title='87',content='87',)

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

class ProuductMixinView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        print("requestrequestrequest30",request)
        return self.list(request,*args,**kwargs)