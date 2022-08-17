from bit import PrivateKeyTestnet
from bit import Key
import environ


env = environ.Env()
environ.Env.read_env()

fromUserPriv = env('FROMUSER_PRIVKEY')
my_key = PrivateKeyTestnet(fromUserPriv)

fromAddrAmount = my_key.get_balance()
fromAddrAmountUsd = my_key.get_balance('usd')

print("from지갑의 잔액 : ", fromAddrAmount)
print("from 지갑의 잔액(usd) : ", fromAddrAmountUsd)


toUserPriv = env('TOUSER_PRIVKEY')
to_key = PrivateKeyTestnet(toUserPriv)

toAddrAmount = to_key.get_balance()
toAddrAmountUsd = to_key.get_balance('usd')

print("to지갑의 잔액 : ", toAddrAmount)
print("to지갑의 잔액(usd) : ", toAddrAmountUsd)


# transaction 발생


# tx_hash = my_key.send([('mqP6vanyhFRzYois4yTpLoCZSkWt7KvxeH', 1, 'usd')])

# print("transaction 발생 ----> : ", tx_hash)
