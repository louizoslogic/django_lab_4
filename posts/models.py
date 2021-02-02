from django.db import models
from django.contrib.auth.models import User

class Chirps(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=128)
    date = models.DateTimeField(null=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.message
