class Human:
    def __init__(self, name):
        print("human initialized")
        self.name = name

    def say_hello(self):
        print(f"hello~ my name is {self.name}")

class Player(Human):
    def __init__(self, name, xp):
        super().__init__(name)
        self.xp = xp


class Fan(Human):
    def __init__(self, name, fav_team):
        super().__init__(name)
        self.fav_team = fav_team


hun_player = Player("hunsman", 1000)
hun_player.say_hello()

hun_fan = Fan("awdawd", "dontknow")
hun_fan.say_hello()

# Human 클래스의 init 메서드를 호출해야만 하는 이유는 Human 클래스는 name이 필요하기 때문이다.
# 4_Inheritance.py 에서 에러가 발생했던 이유는 self.name을 받아오려고하는데, name이라는 값이 없기 때문이다.
# Human 클래스에 name이라는 값이 없는 이유는 init 메서드를 호출하지 않았기 때문이다.

# 따라서 Human 클래스의 init 메서드를 호출하기 위해서는 -> super라는 함수를 사용해야한다. 
# super 함수는 Human 클래스에 접근할 수 있는 권한을 준다.

"""
이 코드에서 하고 있는 건 
1. super라는 함수를 호출하는 것
ㄴ> super는 상속하는 클래스에 접근할 수 있는 권한을 준다.
따라서 상속중인 클래스의 init 메서드를 호출할 수 있다. 이 경우엔 Human인 것.

2. JS나 TS, JAVA, C#과 약간 다르다. 왜냐하면 __init__ 이라는 형식을 가지고 있기 때문. 하지만 로직은 같다.

3. 다른 클래스를 상속할때면, 그 클래스의 constructor를 호출 해야한다. 
ㄴ> 파이썬에서는 super 함수를 사용하여 해당 클래스에 접근할 수 있는 권한을 주게 된다.
ㄴ> 그리고 나서 name과 함께 init 메서드를 호출해준다.
"""