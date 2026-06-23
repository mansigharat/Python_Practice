import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/5")
print(response.json())