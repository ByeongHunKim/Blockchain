from solana.rpc.api import Client
import solana
from solana.account import  Account 
from base58 import b58encode, b58decode
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.system_program import TransferParams, transfer
from solana.transaction import Transaction

client = Client("https://api.devnet.solana.com")


account = Account()
private_key = account.secret_key()
print("1. private_key", private_key)
public_key = bytes(account.public_key())
wallet_address = b58encode(public_key).decode()
print(f"2 DB에 저장될 유저 별 지갑 공개 키: {wallet_address}")
keypair = private_key + public_key
encoded_keypair = b58encode(keypair).decode()
print(f"3 encoded_keypair: {encoded_keypair}")
