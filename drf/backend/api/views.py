
from django.http import JsonResponse
# Create your views here.
import json
def api_home(request,*args,**kwargs):
    body = request.body
    data=json.loads(body)
    print(data.keys())
    print(data.values())
    print(dict(request.headers))
    print(request.content_type)
    ''' header
    {'Content-Length': '15',
     'Content-Type': 'application/json',
      'Host': '127.0.0.1:8000', 
      'User-Agent':
       'python-requests/2.18.4',
        'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
    '''
    #data["headers"]=request.headers
    #data["content_type"]=request.content_type
    #print(body.decode('UTF-8','strict'))
    return JsonResponse({"message":"HI there"})