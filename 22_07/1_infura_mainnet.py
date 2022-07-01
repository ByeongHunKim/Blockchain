# pip install web3 

from web3 import Web3, HTTPProvider
from eth_account import Account
import secrets

web3 = Web3(HTTPProvider("https://mainnet.infura.io/v3/"))

print("web3 - Connection : ", web3.isConnected())

priv = secrets.token_hex(32)
private_key = "0x" + priv
print ("SAVE BUT DO NOT SHARE THIS:", private_key)
acct = Account.from_key(private_key)
print("Address:", acct.address)