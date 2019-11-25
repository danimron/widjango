from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)
    npm = models.CharField(max_length=12)
    angkatan = models.IntegerField()
    status = models.CharField(max_length=20)
    foto = models.URLField()
