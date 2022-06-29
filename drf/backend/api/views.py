
from pyexpat import model
#from django.http import JsonResponse,HttpResponse
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
import json
from products.serializers import ProductSerializer , ProductSerializer_copy

@api_view(["POST"])
def api_home(request,*args,**kwargs):
    print("api_home",request.data)
    data_l=request.data
    model_data=Product.objects.all().order_by("?").first()
    sss = ProductSerializer(data=data_l)
    print("model_datamodel_data",model_data.title)
    data1=ProductSerializer_copy(model_data).data
    #if sss.is_valid():
    return Response(sss.data)
    #data_r = json.dumps(data)
    #return HttpResponse(data_r,headers={"content_type":'application/json'})