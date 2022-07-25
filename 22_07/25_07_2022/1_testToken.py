from web3 import Web3, HTTPProvider,IPCProvider
from web3.middleware import geth_poa_middleware


false = False
true = True




web3 = Web3(HTTPProvider("https://rinkeby.infura.io/v3/bdeb52cede8f45a69bbe940293eb1e72"))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

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

contract = "0x34bfb68cca8d174192f0e1a63ba3fdf50741ac4e"

# tokenContract = web3.eth.contract(address=web3.toChecksumAddress("0x34bfb68cca8d174192f0e1a63ba3fdf50741ac4e"),abi=abi)
# print("1: ", tokenContract)

alice = web3.toChecksumAddress("0xC1F72d2436f6f23384c2d035e509f795450C2434")
bob = web3.toChecksumAddress("0x4617f23881b99201336A98E398299dBd406bEEb2")

# tokenContract.functions.allowance(alice, bob).call()

# tokenContract.functions.balanceOf(bob).call()

# tx_hash = tokenContract.functions.transferFrom(alice, bob, 75).transact({'from': bob})

# tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

# tokenContract.functions.allowance(alice, bob).call()

# test = tokenContract.functions.balanceOf(bob).call()
# print(test)


# alice = web3.toChecksumAddress("0xC1F72d2436f6f23384c2d035e509f795450C2434")
private_key = ""

# test = tokenContract.functions.balanceOf(alice).call()

# print("2: ", test)

# bob = web3.toChecksumAddress("0x4617f23881b99201336A98E398299dBd406bEEb2")

# result = tokenContract.functions.transfer(bob, web3.toWei(100,"ether")).transact({'gas' : 1000000, "from": alice})

# print('3. Txn Hash: ',result.hex())

# transaction  = tokenContract.functions.transfer(bob, 100).transact({'from': alice})
# signed_tx = web3.eth.account.sign_transaction(transaction, private_key)
# print("3: ", tx_receipt)

# txn_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
# print("4: ", txn_hash)


print('----------------------2. 토큰 집금----------------')
tokenContract = web3.eth.contract(address=web3.toChecksumAddress("0x34bfb68cca8d174192f0e1a63ba3fdf50741ac4e"),abi=abi)
unRock = web3.geth.personal.unlockAccount(alice, "private_key", 10)
print('                        unRock: ', unRock)
test = tokenContract.functions.transfer(bob, web3.toWei(2000,"ether")).transact({'gas' : 100000, "from": alice})
print('                        토큰 전송 중...')
print('                        토큰 전송 완료')
rock = web3.geth.personal.lockAccount(alice)
print('                        Rock:   ', rock)
print('       |---------------------------------------------|')
print('Txn Hash: ',test.hex())
print("------------------------------고생하셨습니다!----------------------------------------")