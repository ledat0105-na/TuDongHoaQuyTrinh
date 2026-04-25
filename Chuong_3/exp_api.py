import requests
#viet chuyen thanh ham
def api_get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
   # print(response.text)
api_get_posts()
def api_get_post_by_id(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

api_get_post_by_id(2)
api_get_post_by_id(10)


url = "https://jsonplaceholder.typicode.com/posts"

payload = {'title': 'Lớp 23CT3',
'body': 'test abc',
'userId': '10'}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
