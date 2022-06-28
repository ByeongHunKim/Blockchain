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


# client = Client("https://api.devnet.solana.com")

client = Client("https://snowy-still-flower.solana-mainnet.quiknode.pro/eac6d2984036a3ed91c731c22faddd1b11668992")

# create_associated_token_account 서명자 - 모계좌 == 관리자 
# 대신 지불해는 이유,, 토큰 생태계에 참여하는데 비용을 본인이 지불한다면 .. 거부감이 생길 것 같기 때문. 만약 본인 부담이라면, 0SOL을 보유하고 있는 경우엔 associated_token_account 생성 불가
feePayerWalletAddr = PublicKey("FbKFmRjReeuQMcAxz4LFvhrdghLygNH1tondiyzGQLEQ") # feePayer's public_key
feePayerPriv = "2PPfcxNHuf2kyzddyRFJYQT9P2ThccZyCFo7R4nyAjKBFJMYRLdCsmcupDR3U8CJ5njaQ9PwB4noRtnmx5geT8U4" # feePayer's private_key
feePayerKeypair = b58d(feePayerPriv)
feePayer = Keypair.from_secret_key(feePayerKeypair)

newOwner = '76z2iLit2eyhwfKXH9hRY3S1HNrxsRTQB41FmUumV5rj' # wallet_address = owner가 입력한 wallet_address로 이전 된다.
newOwnerPub = PublicKey(newOwner)
mint1 = 'EXGqHqvKBs4Z1mCwhiGE7kT2TXGFirAjvQzPSQP8nvuw' # mint Address
mintAddr = PublicKey(mint1)

newOwnerPub1 = "Rwi8EySiLEDaHd3m9b8jsZEMKssu6UM65FgBdzrxSgJ"

queryTokenAcc = client.get_token_accounts_by_owner(newOwnerPub1,TokenAccountOpts(mint=mint1))
print(queryTokenAcc)
getTokenAcc = queryTokenAcc['result']['value'][0]['pubkey']
print(f'initialize 완료! {newOwner} 에 연동된 token account 주소는: {getTokenAcc} 입니다.')

