import asyncio
from solana.rpc.async_api import AsyncClient
from solana.publickey import PublicKey
from solana.keypair import Keypair
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
from base58 import b58encode, b58decode
from solana.rpc.types import TokenAccountOpts
from spl.token.instructions import transfer_checked, TransferCheckedParams
 
ENDPOINT = "https://api.devnet.solana.com"
PUBKEY = ""

# D2Qu1V15cmRn9rt3ZXN3GrX4Uuust24v3BjL6VCcbsoN
 
 
async def main():
    async with AsyncClient(ENDPOINT) as client:
        newOwnerPub = PublicKey("")
        newOwnerPub1 = PublicKey("")
        newOwnerPriv = ("")
        newOwnerTokenAddr = ""
        fromAddrKeypair = b58decode(newOwnerPriv)
        signer = Keypair.from_secret_key(fromAddrKeypair)
        mintAddr = PublicKey("")
        connect = await client.is_connected()
        queryTokenAcc = await client.get_token_accounts_by_owner(newOwnerPub,TokenAccountOpts(mint=mintAddr))
        result = queryTokenAcc['result']['value']
        print(result)
        print("솔라나와 연결여부: ", connect)
        if result :
            getTokenAcc = queryTokenAcc['result']['value'][0]['pubkey'] # toaddr
            balance = await client.get_balance(PUBKEY)
            balance1 = await client.get_token_account_balance(getTokenAcc)
            print("추출한 토큰어카운트 주소를 dest 필드에 넣기 : ", getTokenAcc)
            amount = float(10) # 유저가 token 출금페이지에서 입력한 금액 -> dest 값
            transfer_amount = int(amount*(10**9)) # 4. amount = 유저가 token 출금페이지에서 입력한 금액 -> sol -> lamports 단위로 변경필요 -> amount 값
            transaction = Transaction()
            transaction.add(transfer_checked(
                TransferCheckedParams(
                    amount=transfer_amount,
                    decimals=9,
                    dest=PublicKey(getTokenAcc),
                    mint=PublicKey(mintAddr),
                    owner=PublicKey(newOwnerPub1),
                    program_id=TOKEN_PROGRAM_ID,
                    source=PublicKey(newOwnerTokenAddr),
                    )))
            print("6. transaction: ", transaction)
            transaction_result = await client.send_transaction(transaction, signer)
            resultOfTxHash = transaction_result['result']
            print(resultOfTxHash)
        elif result == []:
            print("토큰어카운트 없음 -> 토큰 어카운트 생성 트랜잭션 발생")
            transaction = Transaction()
            create_txn = spl_token.create_associated_token_account(
                payer=newOwnerPub1, owner=newOwnerPub, mint=mintAddr
            )
            transaction.add(create_txn)
            print("4. transaction 값 : ", transaction)
            result = await client.send_transaction(transaction, signer)
            resultOfTxn = result['result']
            print(f"5.txHash = https://solscan.io/tx/{resultOfTxn}?cluster=devnet")
            print("트랜잭션 처리중 .....................20초 소요됩니다.......................")
            # await asyncio.sleep(20)
            queryTokenAcc = await client.get_token_accounts_by_owner(newOwnerPub,TokenAccountOpts(mint=mintAddr))
            getTokenAcc = queryTokenAcc['result']['value'][0]['pubkey']
            print("새로 생성된 토큰어카운트는? :", getTokenAcc)
            amount = float(10)
            transfer_amount = int(amount*(10**9))
            transaction = Transaction()
            transaction.add(transfer_checked(
                TransferCheckedParams(
                    amount=transfer_amount,
                    decimals=9,
                    dest=PublicKey(getTokenAcc),
                    mint=PublicKey(mintAddr),
                    owner=PublicKey(newOwnerPub1),
                    program_id=TOKEN_PROGRAM_ID,
                    source=PublicKey(newOwnerTokenAddr),
                    )))
            print("6. transaction: ", transaction)
            transaction_result = await client.send_transaction(transaction, signer)
            resultOfTxHash = transaction_result['result']
            print(resultOfTxHash)







            
 

 
 
asyncio.run(main())