from django.contrib import admin
from .models import House

# 객체지향에서는 많은 것들을 상속 받을 수가 있다.

# class를 만들었는데, 이 클래스는 ModelAdmin의 모든 걸 상속 받는다. 
# ModelAdmin은 admin 패널이고, 그리고 아래 decorator를 통해 무얼 말하냐면, 
# ㄴ> 이 클래스가 House model을 통제할 것이라고 한 것
# 즉, House model(models.py에서 만든 house 테이블)을 위한 admin 패널을 만든다고 말하고 있는 것.
@admin.register(House)
class houseAdmin(admin.ModelAdmin):

    # 어떻게 admin 패널에 coulmn들을 구현할 것인가?
    list_display = ("name", "price", "address", "pets_allowed")

    # 어떤 column 을 기준으로 필터링 할 것인가?
    list_filter = ("price", "pets_allowed")

    # 어떻게 검색을 가능하게 할 것인가?
    search_fields = ("address",)

    # 어떻게 admin 패널에서 제외 시킬 것인가?
    exclude = ("price",)