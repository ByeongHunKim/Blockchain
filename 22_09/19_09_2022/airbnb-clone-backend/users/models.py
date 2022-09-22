import black
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # column에 옵션 추가하는 방법
    class GenderChoices(models.TextChoices):
        # 이 튜플에는 DB에 들어갈 value, 관리자 페이지에서 보게 될 label이 들어간다.
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    # language 옵션
    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        WON = "won", "Korean Won"
        USD = "usd", "Dollar"

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    profile_photo = models.ImageField(blank=True)
    name = models.CharField(
        max_length=150,
        default="",
    )
    # 일반 사용자인지, 방을 빌려주는 사람인지 분별하기 위한 column
    is_host = models.BooleanField(
        default=False,
    )
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    language = models.CharField(
        max_length=3,
        choices=LanguageChoices.choices,
    )
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
    )
