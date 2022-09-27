from django.db import models
from common.models import CommonModel


class Category(CommonModel):

    """ Room Or Experience Category """
    
    class CategoryKindChoices(models.TextChoices):
        ROOM = "rooms", "Rooms"
        EXPERIENCES = "experiences", "Experiences"

    name = models.CharField(max_length=50,)
    kind = models.CharField(max_length=15, choices=CategoryKindChoices.choices,)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"