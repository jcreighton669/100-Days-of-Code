import requests
from datetime import datetime
from datetime import timedelta

USERNAME = "justincreighton"
TOKEN = "daf3wfsdtsggewfdr3263sfdb"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "ajisai"
}
# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

pixel_add_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.today()
yesterday = today - timedelta(days=1)
yesterday_formatted = yesterday.strftime("%Y%m%d")
add_params = {
    "date": yesterday_formatted,
    "quantity": "15"
}
pixel_post = requests.post(url=pixel_add_endpoint, headers=headers, json=add_params)
print(pixel_post.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday_formatted}"
# delete_response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(delete_response.text)

new_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15"
}
# put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# put_response = requests.put(url=put_endpoint, json=new_pixel_params, headers=headers)
# print(put_response.text)
