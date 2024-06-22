from django.db import models


class Pilot(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        db_table = 'pilot'
        verbose_name = 'Pilot'
        verbose_name_plural = 'Pilots'

    def __str__(self):
        return self.name
