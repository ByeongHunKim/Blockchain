from django.db import models

class CommonModel(models.Model):

    """ Common Model Definition """

    # 중복되는 2개의 field를 가질 예정
    # Django에게 이 model이 DB에 보여지지 않기를 바란다고 말해야한다.
    # 이 모델이 다른 model들이 설계도로 사용하는 model이 되기를 원한다.
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)

    # 이 class는 Django에서 model을 configure 할 때 사용한다.
    # abstact로 되어있으면, model을 봐도 저장하지 않는다. -> 다른 application에서 재사용 가능
    class Meta:
        abstract = True