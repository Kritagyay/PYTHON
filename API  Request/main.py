import requests

response=requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)

data=response.json()
longitude=(data["iss_position"]["longitude"])
latitude = data["iss_position"]["latitude"]
position=(latitude,longitude)
print(position)
