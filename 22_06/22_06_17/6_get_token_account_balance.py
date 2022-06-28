from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.instructions import transfer_checked, TransferCheckedParams

from solana.rpc.commitment import Confirmed
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.transaction import Transaction
from base58 import b58encode, b58decode as b58d
from base64 import b64decode
from pprint import pprint as p

b58e = lambda x: b58encode(x).decode('ascii')
client = Client("https://api.devnet.solana.com")

# token Account
# tokenAcc = "9nLtXAAG6DGUBmnETGSfWpq9iWfDQ21c7X8tXVjYP584"
# result = client.get_token_account_balance(tokenAcc)
# p(result['result']['value']['uiAmount'])

# create_account -> Associated Token Address (ATA)

owner = "4NwS4ezQ3tU4sX26KUmwzKxQwpgwBFMuGYp6U5TBPvc3"
result1 = client.create_account(owner)
p(result1)

transacation = Transaction()
transacation.add(transfer_checked(
    TransferCheckedParams(
        
    )))