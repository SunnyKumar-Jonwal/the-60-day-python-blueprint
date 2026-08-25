import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/comments",
    params={"postId": 1},
    timeout=5,
)
comments = response.json()
print(len(comments))
