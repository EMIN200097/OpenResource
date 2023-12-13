import requests
url="https://place.dog/300/200"
response=requests.get(url)
data=response.json()
print(data)