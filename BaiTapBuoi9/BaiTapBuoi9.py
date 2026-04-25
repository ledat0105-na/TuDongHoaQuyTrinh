import requests

base_url = "https://jsonplaceholder.typicode.com"

# 1. Create - POST /posts
data = {
    "title": "Bai viet moi",
    "body": "Noi dung bai viet moi",
    "userId": 1
}
response = requests.post(f"{base_url}/posts", json=data)
print("POST:", response.status_code, response.json())

# 2. GET /posts
response = requests.get(f"{base_url}/posts")
print("GET all:", response.status_code, response.json()[:2])

# 3. GET /posts/1
response = requests.get(f"{base_url}/posts/1")
print("GET one:", response.status_code, response.json())

# 4. PUT /posts/1
update_data = {
    "id": 1,
    "title": "Cap nhat bai viet",
    "body": "Noi dung moi",
    "userId": 1
}
response = requests.put(f"{base_url}/posts/1", json=update_data)
print("PUT:", response.status_code, response.json())

# 5. DELETE /posts/1
response = requests.delete(f"{base_url}/posts/1")
print("DELETE:", response.status_code)