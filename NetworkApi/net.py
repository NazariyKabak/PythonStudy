import requests

#
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
#
#
# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print(f"Request failed with status code {response.status_code}")
#
#
# data = {'title': 'foo', 'body': 'bar', 'userId': 1}
# response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
#
# if response.status_code == 201:
#     print('Data created: ', response.json())
# else:
#     print(f"Request failed with status code {response.status_code}")
#
# params = {'userId': 1}
# response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
#
# if response.status_code == 200:
#     data = response.json()
#     print(data)
#


# Отримуємо список постів користувачів
response = requests.get('https://jsonplaceholder.typicode.com/posts')

if response.status_code == 200:
    posts = response.json()  # Перетворюємо JSON у Python об'єкт
    for post in posts[:5]:  # Виводимо перші 5 постів
        print(f"Post ID: {post['id']}, Title: {post['title']}")
else:
    print(f"Failed to retrieve posts: {response.status_code}")

#Якщо потрібно фільтрувати дані, можна використовувати параметри запиту
params = {'userId': 1}
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)

if response.status_code == 200:
    posts = response.json()
    for post in posts:
        print(f"Post ID: {post['id']}, Title: {post['title']}")
