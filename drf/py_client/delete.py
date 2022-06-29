
import requests
endpoint="http://127.0.0.1:8000/api/products/update_detroy/3/"

aa=requests.delete(endpoint)
print(aa.json())
