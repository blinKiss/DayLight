import requests

URL_JSON = "https://jsonplaceholder.typicode.com/todos/1"
res = requests.get(URL_JSON)
if(res.status_code == 200):
    print(res.json())