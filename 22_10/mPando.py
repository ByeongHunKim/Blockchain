# web3.py import + IPCProvider는 gethNode 운영할 때, infura같은 blockchain node api 사용할 때는 HTTPProvider 사용
from web3 import Web3, IPCProvider, HTTPProvider

# mPando RPC 주소
web3 = Web3(HTTPProvider("http://13.125.218.17:8545"))

# 네트워크 연결 체크
print("1. web3 - Connection : ", web3.isConnected())

# from_address_pub_key
Addr = ""
print("2. web3 - from_address : ", Addr)

# from_address_priv_key
privKey = ""


toAddr = ""
AddrChecksum = web3.toChecksumAddress(toAddr)
print("3. web3 - to_address : ", toAddr)


balanceOfAddr = web3.eth.getBalance(AddrChecksum)
amount_eth = web3.fromWei(balanceOfAddr, "ether")
print("4. web3 - amount_mPando : ", amount_eth)


nonce = web3.eth.getTransactionCount(AddrChecksum)
print("5. web3 - nonce : ", nonce)


amount_wei = 100000000000000000
print("6. web3 - amount_wei : ", amount_wei)


gas_price = web3.eth.gas_price
print("7. web3 - gas_price : ", gas_price)


tx = {
    "nonce": nonce,
    "to": toAddr,  # 모계좌 주소
    "value": amount_wei,
    "gas": 21000,
    "gasPrice": gas_price,
    "chainId": 24299,
}
signed_tx = web3.eth.account.signTransaction(tx, privKey)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print("8. 트랜잭션 전송 - 확인여부 :", web3.toHex(tx_hash))
txReceipt = web3.eth.waitForTransactionReceipt(tx_hash)
print("9. 트랜잭션 처리 완료 ->>  ", txReceipt)
print("-------------------------전송완료-------------------------------")
