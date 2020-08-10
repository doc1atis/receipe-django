from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.conf import settings
# Create your models here.


class UserManager(BaseUserManager):
    # this is the Method used to create a user --> call it on the User Model
    def create_user(self, email, password=None, **extra_fields):
        # validate anything here
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        # this hashed the password using the hashers specified in setttings.py
        user.set_password(password)
        # this save the user in the database
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=150, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    # this allow us to use the email field as the username ---> must be unique
    USERNAME_FIELD = "email"


class Tag(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.name
