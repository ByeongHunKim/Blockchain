# testnet
from bit import PrivateKeyTestnet

# using .env files 
import environ
env = environ.Env()
environ.Env.read_env()

fromUserPriv = env('FROMUSER_PRIVKEY')
my_key = PrivateKeyTestnet(fromUserPriv)

# btc 단위로 잔액조회
fromAddrAmount = my_key.get_balance('btc')

print(f"1. 조회한 유저의 현재 보유 잔액은 {fromAddrAmount} BTC 입니다.")

