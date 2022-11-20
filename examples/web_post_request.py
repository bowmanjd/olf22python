#!/usr/bin/env python3
"""Example HTTP POST request."""
import json
from urllib.request import Request
from urllib.request import urlopen

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "userid": "1001",
    "title": "POSTing JSON for Fun and Profit",
    "body": "JSON in the request body! Don't forget the content type.",
}
postdata = json.dumps(data).encode()
headers = {"Content-Type": "application/json; charset=UTF-8"}
httprequest = Request(url, data=postdata, headers=headers)

with urlopen(httprequest) as response:
    print(response.read().decode())
