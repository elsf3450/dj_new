
import requests
endpoint="http://127.0.0.1:8000/api/products/UserView/"
#endpoint="http://127.0.0.1:8000/api/products/UserView_append/"
data={
    "username":'bill789',
    "password":"bill123890",
    "user_type":1
}
aa=requests.post(endpoint,json=data)
print(aa)
print(aa.json())
