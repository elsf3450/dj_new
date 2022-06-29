
import requests
endpoint="http://127.0.0.1:8000/api/products/update_detroy/2/"
data={
      "title": "hello_type",
      "price": 300.300,
      

}
aa=requests.put(endpoint,json=data)
print(aa.json())
