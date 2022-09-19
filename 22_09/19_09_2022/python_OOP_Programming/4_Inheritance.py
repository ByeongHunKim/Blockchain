# Human은 Player와 Fan class의 공통된 부분의 코드를 갖게 될 것 (self.name과 say_hello() 메서드 )
class Human:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print(f"hello~ my name is {self.name}")

# 상속을 받기 위해서는 class 옆에 괄호를 열고 상속받은 Class이름을 넣어주면 된다.
class Player(Human):
    def __init__(self, name, xp):
        self.xp = xp

class Fan(Human):
    def __init__(self, name, fav_team):
        self.fav_team = fav_team


hun_player = Player("hunsman", 1000)
hun_player.say_hello()

print(hun_player)
#output -> AttributeError: 'Player' object has no attribute 'name'

# 실제로 Human 클래스의 init 메서드를 호출한 적이 없기 때문에 에러가 발생했다.
# 현재 상황에서는 Human 클래스의 init 메서드를 호출하고 있지 않다.

hun_fan = Fan("husnman", "dontknow")
hun_fan.say_hello()

