from web3 import Web3, HTTPProvider
import time

web3 = Web3(HTTPProvider("https://rinkeby.infura.io/v3/"))

Addr = ""
AddrChecksum = web3.toChecksumAddress(Addr)
balanceOfAddr = web3.eth.getBalance(AddrChecksum)
print(f"1. 현재 지갑 잔액은 ?? = {balanceOfAddr} wei")
value = web3.fromWei(balanceOfAddr,'ether')
print(f"2. 현재 지갑 잔액은 ?? = {value} ETH")
wei2EthUaddr = balanceOfAddr / 1000000000000000000
if wei2EthUaddr >= 0.05:
    print("-"*80)
    print('-------------집금진행')
    gas_price = web3.eth.gas_price
    multiply_gas_price = gas_price * 21000
    print(f"1. 현재 전송 수수료는?? = {multiply_gas_price} wei")
    Addr = "" # userEthAddr userinfo.userPubKey
    privKey = "" # privkey
    nonce = web3.eth.getTransactionCount(AddrChecksum)
    amount_wei = balanceOfAddr - multiply_gas_price
    amount_eth = web3.fromWei(amount_wei,'ether')
    print(f"2.{Addr}지갑에서 깔끔하게 이더리움을 전송하려면 {amount_wei} wei 를 전송하면 됩니다. 이더리움단위로는 {amount_eth} ETH 입니다.")
    tx = {
        'nonce' : nonce,
        'to': '', 
        'value': amount_wei,
        'gas': 21000,
        'gasPrice': gas_price,
        'chainId': 4 
    }
    signed_tx = web3.eth.account.signTransaction(tx, privKey)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    time.sleep(20)
    print("3. 트랜잭션 전송 - 확인여부 :", web3.toHex(tx_hash))
    print('-------------집금완료')
    print("-"*80)