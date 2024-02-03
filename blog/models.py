from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # (auto_now=True) this would update the date posted to the current date time every time the post was updated
    # (auto_now_add=True) this would set to date posted to the current date time only when this object is created,/
    # /with this you can't every update the value of the date posted it will have to keep the exact date time of when/
    # /the post was created
    # (default) we have to import django.utils / timezone to use default./
    # /this will be a date time that takes our timezone setting into consideration. also we don't put parentheses,
    # yes this is a function but we don't want execute that function at that point we just want to pass in the actual/
    # function as a default value
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # this tells to django if user deleted their posts then
    # we want to delete their posts as well

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
