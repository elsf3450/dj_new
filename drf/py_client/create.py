
import requests
endpoint="http://127.0.0.1:8000/api/products/"
data={
    "title":"THIS IS DONE01_last",
    "content":'11_last',
    'price':87,
    "sale_price":"124",

}
aa=requests.post(endpoint,json=data)
print(aa.json())
