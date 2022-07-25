from web3 import Web3, HTTPProvider,IPCProvider

web3 = Web3(HTTPProvider("https://rinkeby.infura.io/v3/bdeb52cede8f45a69bbe940293eb1e72"))

connect = web3.isConnected()

print("1: ", connect)

abi=[
{"constant":True,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},
{"constant":False,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},
{"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},
{"constant":False,"inputs":[{"name":"_addr","type":"address"},{"name":"_value","type":"uint256"},{"name":"_release_time","type":"uint256"}],"name":"addTokenLockDate","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},
{"constant":True,"inputs":[{"name":"_sender","type":"address"}],"name":"lockVolumeAddress","outputs":[{"name":"locked","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},
{"constant":False,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},
{"constant":True,"inputs":[],"name":"note","outputs":[{"name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},
{"constant":True,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":False,"stateMutability":"view","type":"function"},
{"constant":False,"inputs":[{"name":"_value","type":"uint256"}],"name":"burn","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},
{"constant":False,"inputs":[{"name":"_spender","type":"address"},{"name":"_subtractedValue","type":"uint256"}],"name":"decreaseApproval","outputs":[{"name":"success","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},
{"constant":False,"inputs":[{"name":"newAdmin","type":"address"}],"name":"setAdmin","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},
{"constant":True,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},
{"constant":True,"inputs":[{"name":"_addr","type":"address"}],"name":"getMinLockedAmount","outputs":[{"name":"locked","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},
{"constant":True,"inputs":[{"name":"_sender","type":"address"},{"name":"_value","type":"uint256"}],"name":"canTransferIfLocked","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},
{"constant":True,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},
{"constant":True,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},
{"constant":True,"inputs":[{"name":"_sender","type":"address"}],"name":"LockTransferAddress","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},
{"constant":False,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},
{"constant":False,"inputs":[{"name":"_spender","type":"address"},{"name":"_addedValue","type":"uint256"}],"name":"increaseApproval","outputs":[{"name":"success","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},
{"constant":True,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},
{"constant":False,"inputs":[{"name":"_addr","type":"address"},{"name":"_value","type":"uint256"}],"name":"addTokenLock","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},
{"constant":False,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},
{"constant":True,"inputs":[],"name":"admin","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"inputs":[],"payable":False,"stateMutability":"nonpayable","type":"constructor"},
{"payable":True,"stateMutability":"payable","type":"fallback"},
{"anonymous":False,"inputs":[{"indexed":True,"name":"owner","type":"address"},{"indexed":True,"name":"spender","type":"address"},{"indexed":False,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},
{"anonymous":False,"inputs":[{"indexed":True,"name":"to","type":"address"},{"indexed":False,"name":"time","type":"uint256"},{"indexed":False,"name":"amount","type":"uint256"}],"name":"AddTokenLockDate","type":"event"},
{"anonymous":False,"inputs":[{"indexed":True,"name":"to","type":"address"},{"indexed":False,"name":"amount","type":"uint256"}],"name":"AddTokenLock","type":"event"},
{"anonymous":False,"inputs":[{"indexed":True,"name":"burner","type":"address"},{"indexed":False,"name":"amount","type":"uint256"}],"name":"Burn","type":"event"},
{"anonymous":False,"inputs":[{"indexed":True,"name":"previousOwner","type":"address"},{"indexed":True,"name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},
{"anonymous":False,"inputs":[{"indexed":True,"name":"from","type":"address"},{"indexed":True,"name":"to","type":"address"},{"indexed":False,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]

address="0x34bfb68cca8d174192f0e1a63ba3fdf50741ac4e"
address=web3.toChecksumAddress(address)

contract=web3.eth.contract(address=address, abi=abi)

name=contract.functions.name().call()
symbol=contract.functions.symbol().call()
print('2 Name :', name)
print('3 Symbol :', symbol)

dec=contract.functions.decimals().call()
print('4 Decimals :',dec)

dec=10**dec
supply=contract.functions.totalSupply().call()/dec
print(f'5 Total Supply : {supply} {symbol}')


alice = web3.toChecksumAddress("0xC1F72d2436f6f23384c2d035e509f795450C2434")
balance=contract.functions.balanceOf(alice).call()/dec
print(f"6 my Tokens with the contract : {balance} {symbol}")


private_key = ""
acct = web3.eth.account.privateKeyToAccount(private_key)
bob = web3.toChecksumAddress("0x4617f23881b99201336A98E398299dBd406bEEb2")
gas = contract.functions.transfer(bob, 1000).estimateGas({'from': acct.address})
nonce = web3.eth.getTransactionCount('0xC1F72d2436f6f23384c2d035e509f795450C2434')
result = contract.functions.transfer(bob, 1000).buildTransaction({'chainId': 4,
'gas': gas,
'gasPrice': web3.toWei('1', 'gwei'),
'nonce': nonce,})

print(f"7 transaction result  : {result}")

signed_txn = web3.eth.account.signTransaction(result, private_key=private_key)

final = web3.eth.sendRawTransaction(signed_txn.rawTransaction)  

print(f"8 final result  : {final}")




