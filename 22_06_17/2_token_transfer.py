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

# p(feePayerKeypair)
# p(feePayerSign)
# p(feePayer_wallet_address)
# p(fee_payer)

# Fjnn1URmdWwrCqeWVWZKsSYiJCKBj8ZVdKsPLMcDaxv3
feePayer = ''
feePayerKeypair = b58d(feePayer)
feePayerSign = Keypair.from_secret_key(feePayerKeypair)
feePayer_wallet_address = feePayerSign.public_key

print(f"1.feePayerKeypair = {feePayerKeypair}")
print(f"2.feePayerSign = {feePayerSign}")
print(f"3.feePayer_wallet_address = {feePayer_wallet_address}")


fee_payer = Keypair.from_secret_key(b58d(""))
print(f"4.fee_payer = {fee_payer}")

# 4NwS4ezQ3tU4sX26solKUmwzKxQwpgwBFMuGYp6U5TBPvc3
alice = ''
aliceKeypair = b58d(alice)
public_key = aliceKeypair[32:]
private_key = aliceKeypair[:32]
public_key12 = b58e(public_key)

public_key1 = Keypair.from_seed(public_key)
p(public_key1)
aliceSign = Keypair.from_secret_key(aliceKeypair)
alice_wallet_address = aliceSign.public_key

alice1 = Keypair.from_secret_key(b58d(""))


# p(aliceSign.secret_key) # == aliceKeypair
# p(aliceKeypair) # privkey -> b58decode
# p(aliceSign) # privkey -> b58decode 을 바탕으로 키쌍 가지고 있음 내가 원하던 keypair
# p(alice_wallet_address) # -> ''로 감싸져 있지 않은 wallet_address
print(f"5.aliceKeypair = {aliceKeypair}")
print(f"6.aliceSign = {aliceSign}")
print(f"7.alice_wallet_address = {alice_wallet_address}")
print(f"8.alice1 = {alice1}")

mintPubkey = ""

transaction = Transaction()
transaction.add(transfer_checked(
    TransferCheckedParams(
        amount=10000000000,
        decimals=9,
        dest=PublicKey(""),
        mint=PublicKey(""),
        owner=PublicKey(""),
        program_id=TOKEN_PROGRAM_ID,
        source=PublicKey("")
        )))

client = Client("https://api.devnet.solana.com")

print(f"9.transaction = {transaction}")
transaction_result = client.send_transaction(transaction, aliceSign)

resultOfTxhash = transaction_result['result']

print(f"10. txHash = https://solscan.io/tx/{resultOfTxhash}?cluster=devnet")




