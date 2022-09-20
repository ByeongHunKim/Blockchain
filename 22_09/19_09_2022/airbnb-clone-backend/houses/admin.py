from django.contrib import admin
from .models import House

# 객체지향에서는 많은 것들을 상속 받을 수가 있다.

# class를 만들었는데, 이 클래스는 ModelAdmin의 모든 걸 상속 받는다. 
# ModelAdmin은 admin 패널이고, 그리고 아래 decorator를 통해 무얼 말하냐면, 
# ㄴ> 이 클래스가 House model을 통제할 것이라고 한 것
# 즉, House model(models.py에서 만든 house 테이블)을 위한 admin 패널을 만든다고 말하고 있는 것.
@admin.register(House)
class houseAdmin(admin.ModelAdmin):
    pass