import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'
USERNAME = 'kvnkc'
TOKEN = 'kljdslaj287389421yhuiasd'
GRAPHID = 'readinggraph'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# Create pixela user account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_config = {
    'id': GRAPHID,
    'name': 'Reading Graph',
    'unit': 'minutes',
    'type': 'int',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# Creates graph in pixela access graph thru https://pixe.la/v1/users/a-know/graphs/test-graph.html
# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}'

today = datetime.now()
yesterday = datetime(year=2022, month=11, day=2)

pixel_params = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '20'
}

# Adds pixel to graph
# response = requests.post(
#     url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

pixel_update = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime("%Y%m%d")}'

update_parameters = {
    'quantity': '40'
}

# Updates pixel by date on graph
# response = requests.put(
#     url=pixel_update, json=update_parameters, headers=headers)
# print(response.text)

pixel_delete = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{yesterday.strftime("%Y%m%d")}'

# Deletes pixel from graph
# response = requests.delete(url=pixel_delete, headers=headers)
# print(response.text)
