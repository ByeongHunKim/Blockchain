import requests
from requests.structures import CaseInsensitiveDict

url = (
    "https://api-goerli.etherscan.io/api?module=account&action=tokentx&contractaddress="
    + "<ca address>"
    + "&address="
    + "<pubkey address>"
    + "&page=1&offset=100&startblock=0&endblock=latest&sort=asc&apikey=<api key>"
)
print("url은?", url)
headers = CaseInsensitiveDict()
headers["accept"] = "application/json"
resp = requests.get(url, headers=headers)
userTxResult = resp.json()
btc_usdt = userTxResult
print(userTxResult)

# print(len(userTxResult))
