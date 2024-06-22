from django.db import models


class Plane(models.Model):
    name = models.CharField(max_length=20)
    capacity = models.IntegerField()

    class Meta:
        db_table = 'planes'
        verbose_name = 'Plane'
        verbose_name_plural = 'Planes'

    def __str__(self):
        return self.name
