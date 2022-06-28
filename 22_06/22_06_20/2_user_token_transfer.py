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

# 수동 코드
@csrf_exempt
def tokenTransfer(request):
    try:
        test = client.is_connected()
        print("1. 솔라나 연결여부:" ,test)
        mintAuthority = "4NwS4ezQ3tU4sX26KUmwzKxQwpgwBFMuGYp6U5TBPvc3" # owner 고정값
        mintPubkey = "JS3FiJxtv5CYURf7oC9eMPzq21uz1PpsvW9MFfzZDsi" # mint 고정값
        # userID = request.POST.get('userID')
        # print("2. 현재 유저의 id: ",userID)
        # userinfo = SignUp.objects.get(id = userID)
        # print("3. 현재 유저의 정보 :",userinfo)
        # 1. 토큰 어카운트를 소유한 wallet_address
        # 2. fromAddr = userinfo.tokenAcc -> source 값
        # 3. toAddr = 유저가 token 출금페이지에서 입력한 주소 -> dest 값
        # 4. amount = 유저가 token 출금페이지에서 입력한 금액 -> sol -> lamports 단위로 변경필요 -> amount 값
        # 5. decimals = 토큰 정보 받으면 조회해서 몇인지 보면 됨 or solanaLabs 영상에서 decimals 값 추출하는 방법 사용
        # 6. program_id = 맨위에 import 해놓아야함
        #    - from spl.token.constants import TOKEN_PROGRAM_ID
        #    - from spl.token.instructions import transfer_checked, TransferCheckedParams
        context = {'value' : '1','ui_tokenVal' : 'ui_tokenVal'}
        return HttpResponse(json.dumps(context))
    except Exception as error:
        print('실패')
        context = {'valule':'-99'}
        return HttpResponse(json.dumps(context))
