from web3 import Web3, HTTPProvider, IPCProvider

false = False
true = True


web3 = Web3(
    HTTPProvider("https://goerli.infura.io/v3/")
)



abi = 


contract = ""
contractChecksum = web3.toChecksumAddress(contract)
tokenContract = web3.eth.contract(contractChecksum, abi=abi)
print("tokenContract:", tokenContract)
UserAddr = ""
UserAddrChecksum = web3.toChecksumAddress(UserAddr)
uservalueWei = tokenContract.functions.balanceOf(UserAddr).call()  # 유저 토큰 잔액 조회
uservalue = uservalueWei / 1000000000000000000
print("유저잔액얼마?", uservalue)
