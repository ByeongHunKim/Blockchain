from django.db import models

class House(models.Model):

    """Model definition for Houses"""

    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField(verbose_name="price", help_text="Positive numbers only")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True)
    # Foreign Key 타입 사용
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name