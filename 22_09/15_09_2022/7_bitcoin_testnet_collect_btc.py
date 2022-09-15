from bit import PrivateKeyTestnet

import environ

env = environ.Env()
environ.Env.read_env()

# env파일에서 faucet받은 지갑의 비밀키 참조
fromUserPriv = env('TESTUSER_PRIVKEY')
my_key = PrivateKeyTestnet(fromUserPriv)

# 참조되는 비밀키의 잔액을 btc 단위로 조회
fromAddrAmountBtc = my_key.get_balance('btc')
print("fromAddrAmountBtc: ", fromAddrAmountBtc)
# output -> 

# 0.0001 BTC를 전달받을 지갑의 공개키 주소

to_addr = ''


# 모든 보유 BTC를 to_addr에 보내는 코드
tx_hash = my_key.send([], leftover=to_addr)

# 결과값을 알 수 있는 hash 값
print("tx_hash : ", tx_hash)


# 일반적인 transfer 방법 (집금x)
# -------------------------------------------------------
# transaction 발생

# toAddrPub = ''

# tx_hash = my_key.send([(toAddrPub, 1, 'usd')])

# -------------------------------------------------------
