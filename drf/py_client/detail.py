
import requests
endpoint="http://127.0.0.1:8000/api/products/4/"
aa=requests.get(endpoint)
print(aa.json())
