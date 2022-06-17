import struct
from pprint import pprint as p
from solana.rpc.api import Client
from solana.publickey import PublicKey
from solana.transaction import Transaction, AccountMeta
from base58 import b58encode, b58decode as b58d
from base64 import b64decode as b64d
b58e = lambda x: b58encode(x).decode('ascii')

# 토큰 정보 solscan -> https://solscan.io/token/?cluster=devnet

uri = "https://api.devnet.solana.com"

client = Client(uri)

# token address 
token = ""

# token 정보 확인
tokenAccInfo = client.get_account_info(token)
print(f"1. 토큰의 정보 json: {tokenAccInfo}")
account_data = tokenAccInfo['result']['value']['data'][0]
print(f"2. 토큰 데이터에 접근: {account_data}")

# b64decode
data = b64d(account_data)
print(f"3. 토큰의 데이터 b64decode로 추출: {data}")

# mint_authority_option 인데, 무엇을 의미하는 지 모르겠다.
mint_authority_option = struct.unpack("<I", data[0:4])[0]
print(f"4. mint_authority_option: {mint_authority_option}")

# mint token "" 의 authority 주소
mint_authority_decode = struct.unpack("<32s", data[4:36])[0]
mint_authority = b58e(mint_authority_decode)
p(mint_authority_decode)
print(f"5. mint_authority: {mint_authority}")

# token supply -> supply * 10**(-decimal)
token_supply_lamports = struct.unpack("<Q", data[36:44])[0]
token_supply_sol = round(token_supply_lamports*10**(-9),9)
# p(round(token_supply*10**(-9),0)) # -> 1000.0
# p(round(token_supply*10**(-9),9)) # -> 1000.1000001
# p(token_supply_lamports * 10**(-token_decimal)) 
print(f"6. token_supply: {token_supply_sol}")

# decimal 
# p(token_supply_lamports * 10**(-token_decimal)) 
token_decimal = struct.unpack("<B", data[44:45])[0]
print(f"7. token_decimal: {token_decimal}")


