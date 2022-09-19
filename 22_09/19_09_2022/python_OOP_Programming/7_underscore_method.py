
class Dog:
    def __init__(self, name):
        self.name = name

jia = Dog("jia")

print("jia : ", jia)

# OUTPUT -> jia :  <__main__.Dog object at 0x7fd6a7088a90>
# ㄴ> 텍스트로 표현한 값. 이건 메모리 상에서 어디에 위치하고 있는지 말해주고 있다.

# 만약 이걸 받아들일 필요가 없다면?
# ㄴ> 클래스가 문자열로 보이는 방식을 커스텀 할 수 있다면 어떨 거 같나?

# __str__ 이라는 함수를 사용하면 클래스가 문자로 보이는 방식을 바꿀 수 있다.


# -------------------------------------------------------------------------

class Dog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Dog: {self.name}"

hun = Dog("hun")

hunsman = Dog("hunsman")

print("hun: ", hun)
print("hunsman :", hunsman)

# output ->  hun:  Dog: hun , hunsman : Dog: hunsman
# ㄴ> 보다시피 클래스가 문자열로 보이는 방식을 커스텀했다.
# ㄴ> 여기서 str 메서드를 호출하고 있지 않다.
# ㄴ> 내부적으로 파이썬이 이 메서드를 실행시키고 있는 것.
# -------------------------------------------------------------------------


