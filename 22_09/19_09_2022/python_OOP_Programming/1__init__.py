class Player:
    
    def __init__(self):
        # self는 클래스를 가리킨다.
        self.name ="hun"


hun = Player()

print("hun.name : ", hun.name)
# output -> hun.name :  hun

# player의 이름을 다이나믹하게 생성하고 싶다면, self말고 더 많은 parameter를 추가 하는 것