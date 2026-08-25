import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/99999", timeout=5)
print(response.status_code)
