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
fromAddr = "9nLtXAAG6DGUBmnETGSfWpq9iWfDQ21c7X8tXVjYP584"
toAddr = "LarSVMB2UGLkgmHkkjM8jyKeKCRPdJCvvotJtyKMDSp"


mintAuthorityKeypair = b58d(mintAuthorityPriv)
print(f"2.mintAuthorityKeypair = {mintAuthorityKeypair}")
Signer = Keypair.from_secret_key(mintAuthorityKeypair) # == alice1 = Keypair.from_secret_key(b58d("621yVKGcYBMudqUT9AkHpAohXjunWAWMtXz1NyCjK4wa5NCW886kD5z9AL8wRyjxpqB7LwYPMEaw8444da3roMRu"))
print(f"3.트랜잭션 서명자 = {Signer}")

transaction = Transaction()
transaction.add(transfer_checked(
    TransferCheckedParams(
        amount=10000000000,
        decimals=9,
        dest=PublicKey(fromAddr),
        mint=PublicKey(mintPubkey),
        owner=PublicKey(mintAuthority),
        program_id=TOKEN_PROGRAM_ID,
        source=PublicKey(toAddr)
        )))

print(f"4.transaction = {transaction}")
transaction_result = client.send_transaction(transaction, Signer)

resultOfTxhash = transaction_result['result']
print(f"5.txHash = https://solscan.io/tx/{resultOfTxhash}?cluster=devnet")



# 실제 코드
@csrf_exempt
def getBalanceToken(request):
    try:
        test = client.is_connected()
        print("1. 솔라나 연결여부:" ,test)
        userID = request.POST.get('userID')
        print("2. 현재 유저의 id: ",userID)
        userinfo = SignUp.objects.get(id = userID)
        print("3. 현재 유저의 정보 :",userinfo)
        유저의토큰어카운트 = userinfo.유저의 토큰어카운트주소
        print("4. 현재 유저의 토큰어카운트 :",유저의토큰어카운트)
        # 유저의 토큰어카운트가 존재한다면, 현재는 값을 조회할 수 있는 상황
        # 1. get_account_info 하고 value 값에 접근한 후 sol type으로 변환
        # 2. solbalance 컬럼처럼 tokenbalance 컬럼 생성해주고, 그 안에 조회한 값을 저장
        # 3. solVal 처럼 매번 조회되어서 변경되는 값을 저장
        context = {'value' : '1'}
        return HttpResponse(json.dumps(context))
    except Exception as error:
        print('실패')
        context = {'valule':'-99'}
        return HttpResponse(json.dumps(context))




# 수동 코드
@csrf_exempt
def getBalanceToken(request):
    try:
        test = client.is_connected()
        print("1. 솔라나 연결여부:" ,test)
        # userID = request.POST.get('userID')
        # print("2. 현재 유저의 id: ",userID)
        # userinfo = SignUp.objects.get(id = userID)
        # print("3. 현재 유저의 정보 :",userinfo)
        # 유저의토큰어카운트 = userinfo.유저의 토큰어카운트주소
        userTokenAcc = "9nLtXAAG6DGUBmnETGSfWpq9iWfDQ21c7X8tXVjYP584"
        print("2. 현재 유저의 토큰어카운트 :",userTokenAcc)
        # 유저의 토큰어카운트가 존재한다면, 현재는 값을 조회할 수 있는 상황
        # 1. get_account_info 하고 value 값에 접근한 후 sol type으로 변환
        # 2. solbalance 컬럼처럼 tokenbalance 컬럼 생성해주고, 그 안에 조회한 값을 저장
        # 3. solVal 처럼 매번 조회되어서 변경되는 값을 저장
        result = client.get_token_account_balance(userTokenAcc)
        ui_tokenVal = result['result']['value']['uiAmount']
        print("3. 현재 유저의 토큰 잔액은? : ", ui_tokenVal)
        context = {'value' : '1','ui_tokenVal' : 'ui_tokenVal'}
        return HttpResponse(json.dumps(context))
    except Exception as error:
        print('실패')
        context = {'valule':'-99'}
        return HttpResponse(json.dumps(context))