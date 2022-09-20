from django.db import models

class House(models.Model):

    """Model definition for Houses"""

    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    description = models.TextField()
    addreess = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True)