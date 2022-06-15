
import requests
endpoint="http://127.0.0.1:8000/api/"
aa=requests.get(endpoint,params={"abc":123},json={"query":"HI"})
print(aa.text)
print(aa.headers)
print(aa.status_code)