import requests

reply = requests.get('http://localhost:3000')
print(reply.status_code)

print(requests.codes.__dict__)

print(reply.headers)

print(reply.text)


