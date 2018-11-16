import requests
import json

url = 'http://career.wemine.hk/cv-submit'
messages = {"name": "Tung Chi Hung",
            "email": "danieltunghk@gmail.com",
            "position": "Web Developer",
            "cv_url": "https://drive.google.com/open?id=1Qy5RTqvvARG_MiejFgGeYKd_nE1qNv2S"}
headers = {'content-type': 'application/json'}

response = requests.post(url, data=json.dumps(messages), headers=headers)
print(response.status_code, response.reason)
print(messages)
