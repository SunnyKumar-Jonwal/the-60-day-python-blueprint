import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=5)
print(response.status_code)
print(response.json())

missing = requests.get("https://jsonplaceholder.typicode.com/users/9999", timeout=5)
print(missing.status_code)

posts_response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1},
    timeout=5,
)
print(posts_response.url)
posts = posts_response.json()
print(len(posts))

try:
    ok_response = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=5)
    ok_response.raise_for_status()
    print("Request succeeded.")
except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")
