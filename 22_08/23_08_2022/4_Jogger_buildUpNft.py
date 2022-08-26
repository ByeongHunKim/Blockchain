from solana.rpc.api import Client
import solana
from solana.account import  Account 
from base58 import b58encode, b58decode
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.system_program import TransferParams, transfer
from solana.transaction import Transaction


#--------------------------------------------------
# userID = request.POST.get('userID')
# print("2. 현재 유저의 id: ",userID)
# userinfo = SignUp.objects.get(id = userID)
# print("3. 현재 유저의 정보 :",userinfo)
# userPubKey = userinfo.userSolPubKey
# userPrivKey = userinfo.userSolPrivKey
#--------------------------------------------------

client = Client("https://api.devnet.solana.com")

print("---------------------------강화비용 전송 시작--------------------------------")
test = client.is_connected()
print("1. 솔라나 연결여부:" ,test)
userPubKey = ""
userPrivKey = ""
fromAddr = userPubKey # userPubKey
print("2. 보내는 지갑주소 :" ,fromAddr)
fromAddrPriv = userPrivKey
print("3. 보내는지갑 비밀키 :" ,fromAddrPriv)
signKey = b58decode(fromAddrPriv)
print("4. 트랜잭션 서명할 signkey:" ,signKey)
toAddr = "" # 모계좌주소 
# 1SOL = 1000000000 lamport , 1000000 = 0.00001 SOL 인지  최대 수수료를 뺀 유저의 모든 sol 잔액
sol_amount = float(0.999995)
print("9. 보낼 솔라나 금액:" ,sol_amount)
transfer_parameters = TransferParams(
    from_pubkey=PublicKey(fromAddr),
    to_pubkey=PublicKey(toAddr),
    lamports=int(sol_amount*(10**9))
)
sol_transfer = transfer(transfer_parameters)
transaction = Transaction().add(sol_transfer)
transaction_result = client.send_transaction(transaction, Keypair.from_secret_key(signKey))
resultOfTxhash = transaction_result['result']
print("10. txHash값 :", resultOfTxhash)
getBalance = client.get_balance(fromAddr)
lamports = getBalance['result']['value'] 
before_ui_balance = round(lamports*10**(-9),5)
print(f"2. fromAddr before 잔액 : {before_ui_balance} SOL")
print(f"6.txHash = https://solscan.io/tx/{resultOfTxhash}?cluster=devnet")
isConfirmTxn = client.confirm_transaction(resultOfTxhash)
print('7...............Token Transfer 결과: ', isConfirmTxn)
print("---------------------------강화비용 전송 완료--------------------------------")
getBalance = client.get_balance(fromAddr)
lamports = getBalance['result']['value'] 
after_ui_balance = round(lamports*10**(-9),5)
result_of_value = float(before_ui_balance - after_ui_balance)
print(f"6. 유저의 전송 후 남은 보유 SOL 은 {after_ui_balance} SOL 입니다.")
