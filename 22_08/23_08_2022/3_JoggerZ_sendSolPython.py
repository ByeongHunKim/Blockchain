from solana.rpc.api import Client
import solana
from solana.account import  Account 
from base58 import b58encode, b58decode
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.system_program import TransferParams, transfer
from solana.transaction import Transaction

client = Client("https://api.devnet.solana.com")


#------------------------------------------------------ AJAX
# userID = request.POST.get('userID')
# toAddr = request.POST.get('toAddr')
# sol_amount1 = request.POST.get('solamount')
# userinfo = SignUp.objects.get(id = userID)
# userPubKey = userinfo.userSolPubKey
# userPrivKey = userinfo.userSolPrivKey
#------------------------------------------------------ AJAX


print("-----------------------------전송 시작--------------------------------")
test = client.is_connected()
print("1. 솔라나 연결여부:" ,test)

fromAddr = ""
fromAddrPriv = ""
signKey = b58decode(fromAddrPriv) 

toAddr = ""
sol_amount = float(0.999995)


# transaction
transfer_parameters = TransferParams(
    from_pubkey=PublicKey(fromAddr),
    to_pubkey=PublicKey(toAddr),
    lamports=int(sol_amount*(10**9))
)
txFromAddr = transfer_parameters.from_pubkey
txToAddr = transfer_parameters.to_pubkey
txLamport2Sol = round(transfer_parameters.lamports*10**(-9),9)

sol_transfer = transfer(transfer_parameters)
transaction = Transaction().add(sol_transfer)
transaction_result = client.send_transaction(transaction, Keypair.from_secret_key(signKey))
resultOfTxhash = transaction_result['result']
print("5. txHash값 :", resultOfTxhash)
getBalance = client.get_balance(fromAddr)
lamports = getBalance['result']['value'] 
before_ui_balance = round(lamports*10**(-9),5)
print(f"2. fromAddr before 잔액 : {before_ui_balance} SOL")
print(f"6.txHash = https://solscan.io/tx/{resultOfTxhash}?cluster=devnet")
isConfirmTxn = client.confirm_transaction(resultOfTxhash)
print('7...............Token Transfer 결과: ', isConfirmTxn)
print("-----------------------------전송 완료--------------------------------")

getBalance = client.get_balance(fromAddr)
lamports = getBalance['result']['value'] 
after_ui_balance = round(lamports*10**(-9),5)

result_of_value = float(before_ui_balance - after_ui_balance)
print(f"6. 유저의 전송 후 남은 보유 SOL 은 {after_ui_balance} SOL 입니다.")
