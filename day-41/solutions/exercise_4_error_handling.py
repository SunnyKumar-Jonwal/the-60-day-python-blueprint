import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=5)
    response.raise_for_status()
    print("Success")
except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")
