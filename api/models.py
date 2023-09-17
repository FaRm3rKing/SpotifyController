from django.db import models
import string
import random


def generate_unique_code():
    length = 6
    while True:
        code = "".join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code) == 0:
            break
    return code


# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, unique=True, default="")
    host = models.CharField(max_length=50, unique=True)
    allow_skip = models.BooleanField(null=False, default=False)
    required_votes = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)


# you need to turn all these into a JSON that your webapp can use
# you do that with rest_framework serializers
