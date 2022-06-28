# # create solana wallet (phantom , sollet wallet)

# test1 = client.get_account_info("D2oE8PK7zkgNBhPGL6Ro4hctcEStbFZKonZAxStap4zx")

# print("1. 솔라나와 연결여부:" ,test)
# print("1. 계좌 유효여부:" ,test1)
# 솔라나와 연결여부: True

# finalLam = int(1000000000 - 1000000) # 최대 수수료를 뺀 유저의 모든 sol 잔액
# # finalLam2 = int(10000)
# # finalLam3 = int(999900000)
# # finalLam4 = int(999990000 + 10000)
# print('1',finalLam)
# ui_balance = round(finalLam*10**(-9),9)
# print('2',ui_balance)


# ------------------------------------------
sol_amount = float(0.9995)

lamports=int(sol_amount*(10**9))
print('1.결과:',lamports)

# ------------------------------------------

# ------------------------------------------
# sol_amount = 0.99999

# lamports=round(sol_amount*10**(-9),9)
# print('1.결과:',lamports)
# 1.결과: 999990000
# ------------------------------------------