import requests as req

payload = {'website': 'https://abcd.com'}
resp = req.get("http://127.0.0.1:81/hello", params=payload)

print(resp.text)
