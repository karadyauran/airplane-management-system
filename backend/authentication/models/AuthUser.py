import uuid

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class AuthUser(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    is_staff = models.BooleanField(default=False)

    class Meta:
        db_table = 'auth_users'
        verbose_name = 'Auth User'
        verbose_name_plural = 'Auth Users'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'name']

    objects = models.Manager()

    def __str__(self):
        return f'{self.id}: {self.name}'
