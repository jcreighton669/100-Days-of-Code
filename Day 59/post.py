import requests

posts = requests.get("https://api.npoint.io/e9d7761bde7444819f4d").json()
post_objects = []
# print(posts)
for post in posts:
    print(post)
    post_objects.append(post)

for po in post_objects:
    print(po.id)