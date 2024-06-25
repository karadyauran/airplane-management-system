from django.db import models
from django.utils.translation import gettext_lazy as _

from backend.authentication.models.AuthUser import AuthUser


class User(models.Model):
    class Role(models.TextChoices):
        JUNIOR_DISPATCHER = 'JD', _('JUNIOR_DISPATCHER')
        MIDDLE_DISPATCHER = 'MD', _('MIDDLE_DISPATCHER')
        SENIOR_DISPATCHER = 'SD', _('SENIOR_DISPATCHER')

    auth_user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=120, default=auth_user.name)
    role = models.CharField(max_length=12, choices=Role, default=Role.JUNIOR_DISPATCHER)
    q_dispatched = models.IntegerField(default=0)

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.display_name
