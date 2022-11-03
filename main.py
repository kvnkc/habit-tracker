import requests

pixela_endpoint = 'https://pixe.la/v1/users'
USERNAME = 'kvnkc'
TOKEN = 'kljdslaj287389421yhuiasd'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_config = {
    'id': 'graph1',
    'name': 'Reading Graph',
    'unit': 'minutes',
    'type': 'int',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

requests.post(url=graph_endpoint, json=graph_config, headers=headers)
