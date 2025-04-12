from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class PasswordDataUser(AbstractUser):
    def __str__(self):
        return f"username: {self.username}, email: {self.email}"


class PasswordData(models.Model):
    user = models.ForeignKey(PasswordDataUser, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"service: {self.service_name} (username: {self.username}, email: {self.email}. password: {self.password})"
