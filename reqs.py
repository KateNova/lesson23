import requests


url = "http://127.0.0.1:5000/perform_query"

payload = {
  'file_name': 'apache_logs.txt',
  'cmd1': 'filter',
  'value1': 'POST',
  'cmd2': 'map',
  'value2': '0'
}

response = requests.request("POST", url, params=payload)
print('first request:')
print(response.text)


payload = {
  'file_name': 'apache_logs.txt',
  'cmd1': 'map',
  'value1': '0',
  'cmd2': 'unique',
  'value2': ''
}

response = requests.request("POST", url, params=payload)
print('second request:')
print(response.text)


payload = {
  'file_name': 'apache_logs.txt',
  'cmd1': 'filter',
  'value1': 'GET',
  'cmd2': 'limit',
  'value2': '3'
}

response = requests.request("POST", url, params=payload)
print('third request:')
print(response.text)


payload = {
  'file_name': 'apache_logs.txt',
  'cmd1': 'filter',
  'value1': 'POST',
  'cmd2': 'sort',
  'value2': 'asc'
}

response = requests.request("POST", url, params=payload)
print('fourth request:')
print(response.text)
