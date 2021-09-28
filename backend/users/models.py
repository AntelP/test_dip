from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import EmailField, CharField, BooleanField

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = EmailField(max_length=254, unique=True)
    username = CharField(max_length=150)
    first_name = CharField(max_length=150)
    last_name = CharField(max_length=150)
    password = CharField(max_length=150)
    is_superuser = BooleanField(default=False)
    is_blocked = BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_superuser
    