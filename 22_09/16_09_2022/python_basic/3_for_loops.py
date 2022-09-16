from requests import get

"""
websites[0] ... 이렇게 접근하기엔 좀 좋지 않다.
리스트가 얼마나 긴지 신경쓰지 않아도되고 파이썬에게 list의 각 아이템을 활용해서 자동으로 코드를 실행하라고 할 방법을 찾아야한다.
이걸 위해 for 반복문(loop)을 사용할 것.
"""

# for 반복문을 만드는 법

"""
websites 튜플 안에 있는 각각의 item을 사용해서 코드를 실행하고 싶다.
tuple의 각각의 item에 코드를 실행시킬 수 있게 되었다.
이제 궁금한 점은 " 현재 처리 중인 item이 무엇인지 알 수 있는지 " 이다.
list에서 어떤 item을 작업하고 있는지 알기 위해서는 x를 사용하면 된다.
for 반복문을 사용할 때, for는 각각의 item이 실행 될 때 placeholder를 만드는 것을 허락해준다.
placeholder 이름은 내가 원하는대로 만들 수 있다.
"""


websites = (
    "google.com",
    "airbnb.com",
    "twitter.com",
    "facebook.com"
)


results = {}


# 흔한 관습인데, 사람들은 tuple이나 list를 만들 때 복수형을 사용한다. 그리고 for in 에서는 website 같이 단수형으로 쓴다.
for website in websites:
    if not website.startswith("https://"):
        # print("editing website")
        website = f"https://{website}"
    response = get(website)
    if response.status_code == 200:
        results[website] = "OK"
    else:
        results[website] = "FAILED"

print(results)

# output 
# {'https://google.com': 'OK', 'https://airbnb.com': 'FAILED', 'https://twitter.com': 'OK', 'https://facebook.com': 'OK'}