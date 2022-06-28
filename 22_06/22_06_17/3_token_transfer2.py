from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.instructions import transfer_checked, TransferCheckedParams, transfer

from solana.rpc.commitment import Confirmed
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.transaction import Transaction
from base58 import b58encode, b58decode as b58d
from base64 import b64decode
from pprint import pprint as p

client = Client("https://api.devnet.solana.com")

alice1 = Keypair.from_secret_key(b58d(""))

params = transfer_checked(
    source=PublicKey(""),
    dest=PublicKey(""),
    owner=PublicKey(""),
    amount=1000,
    decimals=9,
    mint=PublicKey(""),
    program_id=TOKEN_PROGRAM_ID,
)

p(type(transfer_checked(params)))

p(type(transfer(params)))