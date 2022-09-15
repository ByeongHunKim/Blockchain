# mainnet
from bit import Key

# using .env files 
import environ
env = environ.Env()
environ.Env.read_env()

fromUserPriv = env('MAINNET_PRIVKEY')
my_key = Key(fromUserPriv)

# btc 단위로 잔액조회
fromAddrAmount = my_key.get_balance('btc')

print(f"1. 조회한 유저의 현재 보유 잔액은 {fromAddrAmount} BTC 입니다.")