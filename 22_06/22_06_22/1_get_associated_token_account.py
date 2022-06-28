from solana.publickey import PublicKey
from solana.keypair import Keypair
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Confirmed
from solana.rpc.types import TxOpts
from solana.transaction import Transaction
import solana.system_program as sys

from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.async_client import AsyncToken
from spl.token._layouts import MINT_LAYOUT
import spl.token.instructions as spl_token
import time
from solana.rpc.api import Client
from base58 import b58encode, b58decode as b58d
import asyncio;

client = Client("https://api.devnet.solana.com")


feePayerWalletAddr = "4NwS4ezQ3tU4sX26KUmwzKxQwpgwBFMuGYp6U5TBPvc3" # feePayer's public_key
feePayerPriv = "621yVKGcYBMudqUT9AkHpAohXjunWAWMtXz1NyCjK4wa5NCW886kD5z9AL8wRyjxpqB7LwYPMEaw8444da3roMRu" # feePayer's private_key
feePayerKeypair = b58d(feePayerPriv)
feePayer = Keypair.from_secret_key(feePayerKeypair)
main = PublicKey(feePayerWalletAddr)

newOwner = '2j4uG8nov1P5uozM2TqggHzTJdQ7ysGBtxxNFxhfiEYz' # wallet_address
newOwnerPub = PublicKey(newOwner)
mint1 = 'JS3FiJxtv5CYURf7oC9eMPzq21uz1PpsvW9MFfzZDsi' # mint Address
mintAddr = PublicKey(mint1)



# findnewAcc = client.get_transaction("LJX8Rks6ouRXKiaeEzb2F4N2XdRL2QfpoCD5RkS7bAUGtVZ5cDB4UKLvYoR3Wvvze5nbUbqvgtyNb2dhvFo5GVR")
# newTokenAcc = findnewAcc['result']['transaction']['message']['accountKeys'][1]
# print(newTokenAcc)



# result = client.get_token_accounts_by_owner(main, )
# print(result)

test = client.is_connected()
print("1. 솔라나 연결여부:" ,test)
resultOfTxn = "641rUjSxsgmZJ62FmgiFR4GANPt1oWWKv8qsTjAwL5wgBQ7B11JEb78RbcHsrp4rD5UxACzjiZetd8jAKYETBBxR"
print(resultOfTxn)
result = client.get_transaction(resultOfTxn)
print(result)