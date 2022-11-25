import time

timestamp = time.time()

# 요청하는 시점
timestamp_rounded = round(float(timestamp))

# 요청한 시점에서 24시간 뒤 시간의미 (DB에 저장해야함)
timestamp_24_hours = round(timestamp_rounded + float(86400))

print("timestamp_rounded : ", timestamp_rounded)
print("timestamp_24_hours : ", timestamp_24_hours)

# 요청한 시점이 24시간보다 크면 크다. 작으면 작다
if timestamp_rounded >= timestamp_24_hours:
    print("요청한 시점이 24시간보다 크다 : is_active = 1로 변경 + userinfo.count 값 0으로 재설정(?)")
elif timestamp_rounded < timestamp_24_hours:
    print("요청한 시점이 24시간보다 작다 : is_active = 0으로 유지")
