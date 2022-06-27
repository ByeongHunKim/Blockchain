import requests

from requests.structures import CaseInsensitiveDict

url='https://public-api.solscan.io/account/transactions?account=5dyzXUWNTafkhRS4o9oVRBVgDRrntpZfq2vDEoNAjvoB'

headers = CaseInsensitiveDict()

headers["accept"] = "application/json"

resp = requests.get(url, headers=headers)

print(resp.json())