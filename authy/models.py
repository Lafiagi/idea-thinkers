from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
import os

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password, phone_number):
        if not email:
            raise ValueError("Email cannot be empty.")

        if not first_name:
            raise ValueError("First name must be provided.")

        if not last_name:
            raise ValueError("Last name must be provided.")

        if not password:
            raise ValueError("Password must be provided.")

        if not phone_number:
            raise ValueError("Phone number must be provided.")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,first_name ,last_name, password, phone_number):
        user = self.create_user(email, first_name ,last_name, password, phone_number)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.is_email_verified = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    avatar = models.FileField(blank=True, null=True)
    email = models.EmailField(verbose_name="email", unique=True)
    phone_number = models.CharField(max_length=15, null=False, blank=False, unique=True,)
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    USERNAME_FIELD = "email"

    class Meta:
        ordering = ['date_joined']
        
    @property
    def name(self):
        return self.first_name +" " + self.last_name

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)