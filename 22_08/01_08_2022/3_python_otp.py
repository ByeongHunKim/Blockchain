import pyotp     # pip install pyotp 
import datetime  # 시간 라이브러리

# otp에 사용할 키 - base32 방식 A-Z 2-7까지를 이용하고 = 는 채워야하는 공간 패딩 처리용
otp_key = pyotp.random_base32()
# otp_key = ""
print(otp_key)

# totp 생성
totp = pyotp.TOTP(otp_key)
# 현재 시간 얻기
now = datetime.datetime.now()

# 현재 시간 출력
print('current time : ', now)
# totp.at을 이용한 TOTP 값 출력, totp.now를 이용한 출력
print("now totp.at: " +  str(totp.at(datetime.datetime.now())) + ", totp.now : " + totp.now())
# 현재 시간에 30초를 더해서 totp.at으로 30초 후 OTP 값을 출력
print('next otp : ', totp.at(int(now.timestamp())+30))