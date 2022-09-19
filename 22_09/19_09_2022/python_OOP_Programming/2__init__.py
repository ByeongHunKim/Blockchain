class Player:
    
    def __init__(self, name, xp):
        # player의 이름을 다이나믹하게 생성하고 싶다면, self말고 더 많은 parameter를 추가 하는 것
        # 모든 메서드는 self를 가장 첫번째 parameter로 한다는 것이 중요하다.
        # 모든 python class안에 있는 모든 메서드는 첫번째 인자로 self를 넘겨받을 것
        self.name = name
        self.xp = xp

    def say_hello(self):
        print(f"hello~ my name is {self.name}")


hun = Player("hunsman", 1000)
print(hun.name, hun.xp)
# output -> hunsman 1000

hun.say_hello()
# output -> hello~ my name is hunsman


