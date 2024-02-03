from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # cascade means if the user is deleted then also
    # delete the profile. but if we delete the profile it won't delete the user. it's just one way thing.
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return '{un} Profile'.format(un={self.user.username})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
