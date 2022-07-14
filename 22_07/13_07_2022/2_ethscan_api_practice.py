import requests 
from requests.structures import CaseInsensitiveDict


userSolAddr = "0xC1F72d2436f6f23384c2d035e509f795450C2434"
# "https://api-rinkeby.etherscan.io/api?module=account&action=balance&address=0xC1F72d2436f6f23384c2d035e509f795450C2434&tag=latest&apikey="
url="https://api-rinkeby.etherscan.io/api?module=account&action=txlist&address="+userSolAddr+"&startblock=0&endblock=999999999&page=1&offset=500&sort=asc&apikey="
print("url은?",url)
headers = CaseInsensitiveDict()
headers["accept"] = "application/json"
resp = requests.get(url, headers=headers)
userTxResult = resp.json()
print(userTxResult)
