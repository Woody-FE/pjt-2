from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


User = settings.AUTH_USER_MODEL

class CustomUser(AbstractUser):
    child_name = models.CharField(max_length=20, blank=True, null=True)
    child_image = ProcessedImageField(
        upload_to='image/child/%Y/%m/%d',
        format='JPEG',
        blank=True,
        null=True
    )
    child_gender = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return "User: {}".format(self.email)


class Family(models.Model):
    name = models.CharField(max_length=10)
    image = ProcessedImageField(
        upload_to='image/family',
        processors=[Thumbnail(100, 100)],
        format='JPEG',
        options={
            'quality': 50
        }
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='families')
    # mycharacter
    gender = models.CharField(max_length=10)

    def __str__(self):
        return "Family: {} of {}".format(self.name, self.user.email)