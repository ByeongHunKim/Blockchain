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
from solana.rpc.types import TokenAccountOpts


client = Client("https://api.devnet.solana.com")


newOwner = 'D2oE8PK7zkgNBhPGL6Ro4hctcEStbFZKonZAxStap4zx' # wallet_address = owner가 입력한 wallet_address로 이전 된다.
newOwnerPub = PublicKey(newOwner)
mint1 = 'JS3FiJxtv5CYURf7oC9eMPzq21uz1PpsvW9MFfzZDsi' # mint Address
mintAddr = PublicKey(mint1)


queryTokenAcc = client.get_token_accounts_by_owner(newOwnerPub,TokenAccountOpts(mint=mintAddr))
print(queryTokenAcc)
getTokenAcc = queryTokenAcc['result']['value'][0]['pubkey']
print(f'initialize 완료! 입력한주소 에 연동된 token account 주소는: {getTokenAcc} 입니다.')

