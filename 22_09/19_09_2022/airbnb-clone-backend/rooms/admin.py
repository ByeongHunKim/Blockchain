from django.contrib import admin
from .models import Room, Amenity

# 이 클래스가 어떤 model을 컨트롤할 것인지 명시
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass