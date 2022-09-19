class Player:
    
    def __init__(self, name, xp):
        # player의 이름을 다이나믹하게 생성하고 싶다면, self말고 더 많은 parameter를 추가 하는 것
        # 모든 메서드는 self를 가장 첫번째 parameter로 한다는 것이 중요하다.
        # 모든 python class안에 있는 모든 메서드는 첫번째 인자로 self를 넘겨받을 것
        self.name = name
        self.xp = xp

    def say_hello(self):
        print(f"hello~ my name is {self.name}")

# 새로운 class

class Fan:
    def __init__(self, name, fav_team):
        self.name = name
        self.fav_team = fav_team
    
    def say_hello(self):
        print(f"hello my name is {self.name}")

hun = Fan("hunsman", "testc")

print(hun.say_hello())

# 상속을 활용하여 이 두 class에서 반복적인 부분을 추상화 하는 것 -> 그러면 코드가 더 깔끔해진다.

"""
뭐가 반복되고 있을까?
ㄴ> self.name이 반복이고 , say_hello가 반복되고 있다.

따라서 반복되는 코드를 저장할 다른 class를 만드는 작업이 필요하다.
"""