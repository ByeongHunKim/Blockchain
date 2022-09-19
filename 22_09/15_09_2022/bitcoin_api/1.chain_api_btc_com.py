import requests 
from requests.structures import CaseInsensitiveDict


# mainnet 생성 지갑 조회 
userBtcAddr = "16SNBd6rez2hAgEdhb6V4EShETRfdSpVE8"
motherBtcAddr = "1FHwud81Czwe6ujMHGtu5bidmd3pbP7pSc"
url="https://chain.api.btc.com/v3/address/"+userBtcAddr+"/tx"

print("url은?",url)
headers = CaseInsensitiveDict()
headers["accept"] = "application/json"
resp = requests.get(url, headers=headers)
txfee_list = resp.json()
# print(txfee_list)


# 데이터 접근 방법 기록들

# -------------------------------------------------------

# print(txfee_list['data']['list'][0])
tx_fee = txfee_list['data']['list']

# print(tx_fee[0]['outputs'][1]['addresses'][0])

# print(tx_fee[0])

for i in tx_fee:
    time = i["block_time"]
    hash = i["hash"]
    from_addr = i['inputs'][0]['prev_addresses'][0]
    to_addr = i['outputs']
    for i in to_addr:
        print("to addr : ", i['addresses'][0])
        to = i['addresses'][0]
        # if to == userBtcAddr or to == motherBtcAddr:
        if to == userBtcAddr:
            print("to_addr 조회성공")
            # to_address : 받는 주소
            to_address = to
            # value : 받은 금액 (BTC 단위)
            value = i['value'] / 100000000
            print("value:", value)
            print("to_address:", to_address)
            # 원하는 값 도출 시 for문 중지
            print("time: ", time)
            print("hash: ", hash)
            print("from_addr: ", from_addr)
            # print("to_addr: ", to_addr)
            print('/')
            break
# -------------------------------------------------------

# 9월 15일 목요일 14시 40분 현재 output ( 메인넷 집금에 사용할 BTC 전달받지 못함)
# {'data': {'list': None, 'page': 1, 'page_total': 0, 'pagesize': 10, 'total_count': 0}, 'err_code': 0, 'err_no': 0, 'message': 'success', 'status': 'success'}
