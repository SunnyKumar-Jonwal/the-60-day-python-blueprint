import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=5)
print(response.status_code)
print(response.json())
