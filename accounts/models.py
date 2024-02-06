from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self,username, email, password=None):
        if not username:
            raise TypeError('Enter email')
        if not email:
            raise TypeError('Enter Password')

        user = User(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,username,email,password):
        if not password:
            raise TypeError('Password cannot be none')
        user = self.create_user(username,email,password)
        user.is_staff=True
        user.is_superuser=True
        user.save()
        return True


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=40,unique=True)
    username = models.CharField(max_length=40, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        return self.email