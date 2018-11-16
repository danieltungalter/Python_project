import requests
import json

url = 'http://career.wemine.hk/cv-submit'
messages = {"name": " ",
            "email": " ",
            "position": " ",
            "cv_url": " "}
headers = {'content-type': 'application/json'}

response = requests.post(url, data=json.dumps(messages), headers=headers)
print(response.status_code, response.reason)
print(messages)
