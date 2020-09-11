from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    child_name = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)

    def __str__(self):
        return "User: {}".format(self.email)