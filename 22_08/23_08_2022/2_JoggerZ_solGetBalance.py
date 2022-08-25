from solana.rpc.api import Client
import solana
from solana.account import  Account 
from base58 import b58encode, b58decode
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.system_program import TransferParams, transfer
from solana.transaction import Transaction

client = Client("https://api.devnet.solana.com")


addr = ""

getBalance = client.get_balance(addr)
lamports = getBalance['result']['value']
print("1. 유저의 지갑주소 :", addr)
getBalance = client.get_balance(addr)
lamports = getBalance['result']['value'] 
print(f"2. 유저의 지갑조회 - lamport 단위 : {lamports} lamports")
ui_balance = round(lamports*10**(-9),5)
print(f"3. 유저의 지갑조회 - SOL 단위 : {ui_balance} SOL")