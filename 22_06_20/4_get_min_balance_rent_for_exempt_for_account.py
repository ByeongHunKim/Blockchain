import solana.system_program as sp
from solana.publickey import PublicKey
from solana.account import Account 
from solana.rpc.api import Client
from spl.token.constants import TOKEN_PROGRAM_ID
from solana.transaction import Transaction
from base58 import b58encode, b58decode as b58d
from solana.keypair import Keypair
from solana.rpc.types import TxOpts

client = client = Client("https://api.devnet.solana.com")

mintAuthority = "" 
mintAuthorityPriv = "" # DB에 있는 유저별 privKey 
mintAuthorityKeypair = b58d(mintAuthorityPriv)
feePayer = Keypair.from_secret_key(mintAuthorityKeypair)
# new_public_key = new_account.public_key()
# print("1. 생성한 token acccount: ", new_public_key)
account = Account()
secretKey = account.secret_key()
bytesaccount = bytes(account.public_key())
address_public = b58encode(bytesaccount).decode()
make_privateKey = secretKey + bytesaccount
realprivate_key = b58encode(make_privateKey).decode()
print(realprivate_key)
mintAuthorityKeypair2 = b58d(realprivate_key)
feePayer2 = Keypair.from_secret_key(mintAuthorityKeypair2)

fee = client.get_minimum_balance_for_rent_exemption(165)["result"]
print("2. 생성한 token account에 rent fee: ", fee)


params = sp.CreateAccountParams(
    from_pubkey=PublicKey(mintAuthority),
    new_account_pubkey=PublicKey(address_public),
    lamports=fee,
    space=165,
    program_id=TOKEN_PROGRAM_ID
)

print("3. params 값 : ", params)

transaction = Transaction()
transaction.add(
    sp.create_account(params)
)

print("4. transaction 값 : ", transaction)

# opts = TxOpts(skip_confirmation=False)
# print ("Please wait for confirmation ...")

result = client.send_transaction(transaction, feePayer, feePayer2)

print("5. 트랜잭션 완료 : ", result)
