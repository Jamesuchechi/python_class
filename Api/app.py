import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

try:
	response = requests.get(url, timeout=10)
	response.raise_for_status()
	print(response.status_code)
	print(response.json())
except requests.exceptions.RequestException as error:
	print(f"Request failed: {error}")
