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

AsyncClient1 = Client("https://api.devnet.solana.com")

test = AsyncClient1.is_connected()

print("1. 솔라나와 연결여부:" ,test)

feePayerWalletAddr = "" # feePayer's public_key
feePayerPriv = ""  # feePayer's private_key
feePayerKeypair = b58d(feePayerPriv)
feePayer = Keypair.from_secret_key(feePayerKeypair)
feePayerPub = feePayer.public_key


newOwner = '' # wallet_address
newOwnerPub = PublicKey(newOwner)
mint1 = '' # mint Address
mintAddr = PublicKey(mint1)

async def create_associated_token_account(
    client: AsyncClient,
    payer: Keypair,
    owner: PublicKey,
    mint: PublicKey
) -> PublicKey:
    txn = Transaction()
    create_txn = spl_token.create_associated_token_account(
        payer=feePayerPub, owner=newOwnerPub, mint=mintAddr
    )
    txn.add(create_txn)
    await client.send_transaction(txn, payer, opts=TxOpts(skip_confirmation=False, preflight_commitment=Confirmed))
    return create_txn.keys[1].pubkey


create_associated_token_account(AsyncClient1, feePayer, newOwnerPub, mintAddr)