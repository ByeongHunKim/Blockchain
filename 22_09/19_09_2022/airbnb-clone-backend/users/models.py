from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150, default="")
    # 일반 사용자인지, 방을 빌려주는 사람인지 분별하기 위한 column
    is_host = models.BooleanField(default=False)