# 파이썬을 사용할 때의 OOP에서 상속에 대해 복습

# super 함수의 사용과 중요성을 이해하는 것이 아주 중요하다.

# -------------------------------------------------------------------------

# class Dog:
#     def __init__(self, dog):
#         self.dog = dog

# class Beagle(Dog):
#     def __init__(self,dog):
#         super().__init__(dog)

# beagle = Beagle("corgi")
# print(beagle.dog)

# -------------------------------------------------------------------------


class Dog:
    def woof(self):
        print("woof woof")

class Beagle(Dog):
    def woof(self):
        super().woof
        print("super woof")

beagle = Beagle()
beagle.woof()

# output -> woof woof
# Dog 클래스에서 init 함수를 가지고 있다. 어디에서도 속성을 정의하고 있지 않기 때문.
# 속성을 정의할 때만 init 메서드를 사용하면 된다.