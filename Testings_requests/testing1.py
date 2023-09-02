import requests
import json
import pprint
import sys

with open("myFIle.jpg", "rb") as f:
    response = requests.post("http://127.0.0.1:8000/upload/", files={"file": f})

print(response.json())
