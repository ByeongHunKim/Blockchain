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

# create_associated_token_account 서명자 - 모계좌 == 관리자 
# 대신 지불해는 이유,, 토큰 생태계에 참여하는데 비용을 본인이 지불한다면 .. 거부감이 생길 것 같기 때문. 만약 본인 부담이라면, 0SOL을 보유하고 있는 경우엔 associated_token_account 생성 불가
feePayerWalletAddr = PublicKey("") # feePayer's public_key
feePayerPriv = "" # feePayer's private_key
feePayerKeypair = b58d(feePayerPriv)
feePayer = Keypair.from_secret_key(feePayerKeypair)
newOwner = '' # 2TYjQTbF9tj6qhzw9D4E6yb3VB8pfdwe819CtXqE9d2S
newOwnerPub = PublicKey(newOwner)
mint1 = '' # mint Address
mintAddr = PublicKey(mint1)

queryTokenAcc = client.get_token_accounts_by_owner(newOwnerPub,TokenAccountOpts(mint=mint1))
getTokenAcc = queryTokenAcc['result']['value']
print("처음 유저의 토큰 어카운트 조회결과 : ",getTokenAcc)
tokenAccLen = len(getTokenAcc)
print(tokenAccLen)
# 만약 유저가 종류별 토큰을 가지고 있는 경우의 length 는 어떨까 반복문을 돌면서 tokenaddress를 일치하는 걸 찾아야한다.
if tokenAccLen == 0 :
    print("--------------------토큰어카운트생성-------------------------------------------")
    transaction = Transaction()
    create_txn = spl_token.create_associated_token_account(
        payer=feePayerWalletAddr, owner=newOwnerPub, mint=mintAddr
    )
    transaction.add(create_txn)

    result = client.send_transaction(transaction, feePayer)
    resultOfTxn = result['result']
    print(f"txHash 결과 == https://solscan.io/tx/{resultOfTxn}?cluster=devnet")

    print('initialize 진행중.........................')
    time.sleep(20)
    queryTokenAcc = client.get_token_accounts_by_owner(newOwnerPub,TokenAccountOpts(mint=mint1))
    getTokenAcc = queryTokenAcc['result']['value'][0]['pubkey']
    print(f'initialize 완료! {newOwner} 에 연동된 token account 주소는: {getTokenAcc} 입니다.')
else :
    getTokenAcc = queryTokenAcc['result']['value'][0]['pubkey']
    print("이미 토큰 어카운트가 존재합니다. : ", getTokenAcc)
    # userinfo.tokenAcc = getTokenAcc
    # userinfo.save()
