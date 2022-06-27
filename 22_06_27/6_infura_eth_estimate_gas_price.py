from web3 import Web3, HTTPProvider
import statistics
web3 = Web3(HTTPProvider("https://rinkeby.infura.io/v3/bdeb52cede8f45a69bbe940293eb1e72"))

print("web3 - 연결여부 :", web3.isConnected())
tx = "0xebfa0979e175b6104393b653d0587bf0d08f6a2ee5e10cd4b65b1f43ede41e28 "
pending_transactions = web3.provider.make_request(tx, [])
print(pending_transactions)
gas_prices = []
gases = []
# for tx in pending_transactions["result"[:10]]:
# 	gas_prices.append(int((tx["gasPrice"]),16))
# 	gases.append(int((tx["gas"]),16))

print("Average:")
print("-"*80)
print("gasPrice: ", statistics.mean(gas_prices))
print(" ")
print("Median:")
print("-"*80)
print("gasPrice: ", statistics.median(gas_prices))