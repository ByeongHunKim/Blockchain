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

mintAuthority = "4NwS4ezQ3tU4sX26KUmwzKxQwpgwBFMuGYp6U5TBPvc3" 
mintAuthorityPriv = '621yVKGcYBMudqUT9AkHpAohXjunWAWMtXz1NyCjK4wa5NCW886kD5z9AL8wRyjxpqB7LwYPMEaw8444da3roMRu' # DB에 있는 유저별 privKey 
mintPubkey = "JS3FiJxtv5CYURf7oC9eMPzq21uz1PpsvW9MFfzZDsi"
toAddr = "4fQ6RFbzisF6RCFksS4izhDkKiM3ycSg5u8r93wqHoHN"
fromAddr = "LarSVMB2UGLkgmHkkjM8jyKeKCRPdJCvvotJtyKMDSp"


mintAuthorityKeypair = b58d(mintAuthorityPriv)
print(f"2.mintAuthorityKeypair = {mintAuthorityKeypair}")
Signer = Keypair.from_secret_key(mintAuthorityKeypair) # == alice1 = Keypair.from_secret_key(b58d("621yVKGcYBMudqUT9AkHpAohXjunWAWMtXz1NyCjK4wa5NCW886kD5z9AL8wRyjxpqB7LwYPMEaw8444da3roMRu"))
print(f"3.트랜잭션 서명자 = {Signer}")

transaction = Transaction()
transaction.add(transfer_checked(
    TransferCheckedParams(
        amount=10000000000,
        decimals=9,
        dest=PublicKey(toAddr),
        mint=PublicKey(mintPubkey),
        owner=PublicKey(mintAuthority),
        program_id=TOKEN_PROGRAM_ID,
        source=PublicKey(fromAddr)
        )))

print(f"4.transaction = {transaction}")
transaction_result = client.send_transaction(transaction, Signer)

resultOfTxhash = transaction_result['result']
print(f"5.txHash = https://solscan.io/tx/{resultOfTxhash}?cluster=devnet")




