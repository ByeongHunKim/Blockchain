# pip install web3 

from web3 import Web3, HTTPProvider
from eth_account import Account
import secrets

# web3 = Web3(HTTPProvider("https://mainnet.infura.io/v3/"))
web3 = Web3(HTTPProvider("https://rinkeby.infura.io/v3/"))

print("web3 - Connection : ", web3.isConnected())

# getPrice = web3.eth.gasPrice;
# print("10(외부전송).가스비 조회: ", getPrice)

gas_price = web3.eth.gas_price
multiply_gas_price = gas_price * 21000
print(f"1. 현재 전송 수수료는?? = {multiply_gas_price} wei")

Addr = ""
privKey = "" # privkey
AddrChecksum = web3.toChecksumAddress(Addr)
nonce = web3.eth.getTransactionCount(AddrChecksum)
balanceOfAddr = web3.eth.getBalance(AddrChecksum)

amount_wei = balanceOfAddr - multiply_gas_price
amount_eth = web3.fromWei(amount_wei,'ether')
print(f"2.{Addr}지갑에서 깔끔하게 이더리움을 전송하려면 {amount_wei} wei 를 전송하면 됩니다. 이더리움단위로는 {amount_eth} ETH 입니다.")


tx = {'nonce': nonce,
      'to': '', # to address
      'value': amount_wei,
      'gas': 21000,
      'gasPrice': gas_price,
      'chainId': 4
      }

signed_tx = web3.eth.account.signTransaction(tx, privKey)
print("6. 트랜잭션 - 확인여부 :", signed_tx)

tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print("7. 트랜잭션 전송 - 확인여부 :", web3.toHex(tx_hash))