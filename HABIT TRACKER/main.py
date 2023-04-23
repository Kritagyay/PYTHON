import requests
import datetime

TODAY=datetime.datetime.today()
# print(now.strftime("%Y%m%d"))

TOKEN="sdnusbdvsbvislicns"
NAME="kritagyay"
GRAPH_ID="graph1"

URL="https://pixe.la/v1/users"

user_parmas={
    "token":TOKEN,
    "username":NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# responses=requests.post(url=URL,json=user_parmas)
# print(responses.text)

graph_endpoint=f"{URL}/{NAME}/graphs"

graph_params={
    "id":GRAPH_ID,
    "name":"Cycling Graph",
    "unit":"Km",
    "type": "float",
    "color":"ajisai"
}
headers={
    "X-USER-TOKEN":TOKEN
}
# responses=requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(responses.text)

post_endpoint=f"{graph_endpoint}/{GRAPH_ID}"

post_params={
    "date":TODAY.strftime("%Y%m%d"),
    "quantity":input("How many kilometers you have cycled?"),
}

responses=requests.post(url=post_endpoint,json=post_params,headers=headers)
print(responses.text)

update_endpoint=f"{post_endpoint}/{TODAY.strftime('%Y%m%d')}"

update_params={
    "quantity":"25",
    }

# responses=requests.put(url=update_endpoint,json=update_params,headers=headers)
# print(responses.text)

delete_endpoint=f"{update_endpoint}"

# responses=requests.delete(url=delete_endpoint,headers=headers)
# print(responses.text)