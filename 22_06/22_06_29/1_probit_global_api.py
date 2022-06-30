import requests

url = "https://accounts.probit.com/token"

payload = {"grant_type": "client_credentials"}
headers = {
    "Accept": "application/json",
    "Authorization": "",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)