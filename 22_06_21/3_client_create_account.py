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


feePayerWalletAddr = "" # feePayer's public_key
feePayerPriv = "" # feePayer's private_key
feePayerKeypair = b58d(feePayerPriv)
feePayer = Keypair.from_secret_key(feePayerKeypair)

newOwner = '' # wallet_address = owner가 입력한 wallet_address로 이전 된다.
newOwnerPub = PublicKey(newOwner)
mint1 = '' # mint Address
mintAddr = PublicKey(mint1)


transaction = Transaction()
create_txn = spl_token.create_associated_token_account(
    payer=feePayerWalletAddr, owner=newOwnerPub, mint=mintAddr
)
transaction.add(create_txn)

result = client.send_transaction(transaction, feePayer)
resultOfTxn = result['result']
print(f"txHash 결과 == https://solscan.io/tx/{resultOfTxn}?cluster=devnet")

# https://solscan.io/tx/x3a6sPpU22PDWNU16Lgm16ywSM1s364WbzhGukNTEcTgBpSxPXHTwLvTN7V81LCER2rhyuvenLqRB2nUAm4AZSB?cluster=devnet