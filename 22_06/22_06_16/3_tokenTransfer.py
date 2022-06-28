from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.instructions import transfer_checked, TransferCheckedParams

from solana.rpc.commitment import Confirmed
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.transaction import Transaction
from base58 import b58encode, b58decode


# Fjnn1URmdWwrCqeWVWZKsSYiJCKBj8ZVdKsPLMcDaxv3
feePayer = "237Vv8DrGKK8GqyBmSMdhuBtqFi4nUgGMYjYad5NYQiAE5rPYkqVzqDYPcu26Ts9NdJ6SYHWSD52BcukQMZBoKAf"
feePayerKeypair = b58decode(feePayer)
feePayerPub = feePayerKeypair[32:]
# print(b58encode(feePayerPub).decode())

# 4NwS4ezQ3tU4sX26KUmwzKxQwpgwBFMuGYp6U5TBPvc3
alice = "621yVKGcYBMudqUT9AkHpAohXjunWAWMtXz1NyCjK4wa5NCW886kD5z9AL8wRyjxpqB7LwYPMEaw8444da3roMRu"
aliceKeypair = b58decode(alice)

mintPubkey = "JS3FiJxtv5CYURf7oC9eMPzq21uz1PpsvW9MFfzZDsi"

transaction = Transaction()
transaction.add(
    transfer_checked(
        TransferCheckedParams(
    program_id=TOKEN_PROGRAM_ID,
    source=PublicKey("LarSVMB2UGLkgmHkkjM8jyKeKCRPdJCvvotJtyKMDSp"),
    mint=PublicKey("JS3FiJxtv5CYURf7oC9eMPzq21uz1PpsvW9MFfzZDsi"),
    dest=PublicKey("9nLtXAAG6DGUBmnETGSfWpq9iWfDQ21c7X8tXVjYP584"),
    owner=PublicKey("4NwS4ezQ3tU4sX26KUmwzKxQwpgwBFMuGYp6U5TBPvc3"),
    amount=100,
    decimals=9,
    signers=[feePayer, alice]
        )
    )
)
client = Client(endpoint="https://api.devnet.solana.com", commitment=Confirmed)
owner = "b58encode(feePayerPub).decode()" # <-- need the keypair for the token owner here! 5j22en4YDzDNzmGm7WWVxxYGDQ3Y873p7joVbKncZ1Ke
client.send_transaction(
    transaction, owner, opts=TxOpts(skip_confirmation=False, preflight_commitment=Confirmed))


# curl https://solana-devnet-rpc.allthatnode.com/ZYacGTC1847qCjJHnG2sgJBoX02twlMU \
# --request POST \
# --header "Content-Type: application/json" \
# --data '{"jsonrpc":"2.0","id":1, "method":"getBlockHeight"}'

