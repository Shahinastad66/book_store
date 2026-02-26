from  django.contrib.auth.models import AbstractUser, PermissionsMixin, AbstractBaseUser, UserManager
from django.db import models
from django.conf import settings



class CustomUserManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class AllObjectsUserManager(UserManager):
    def get_queryset(self):
        return super().get_queryset()

class User(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True)
    national_code = models.CharField(max_length=10, unique=True, null=True, blank=True)
    birth_day = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    objects = CustomUserManager()
    all_objects = AllObjectsUserManager()

class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')
    national_code = models.CharField(max_length=10)

    def __str__(self):
        return self.national_code

class Author2(Author):
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    class Meta:
        proxy = True
