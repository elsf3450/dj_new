
from pyexpat import model
from django.http import JsonResponse,HttpResponse
from products.models import Product
# Create your views here.
import json
def api_home(request,*args,**kwargs):
    model_data=Product.objects.all().order_by("?").first()
    data={}
    data['id']=model_data.id
    data['title']=model_data.title
    data['content']=model_data.content

    data_r = json.dumps(data)
    return HttpResponse(data_r,headers={"content_type":'application/json'})