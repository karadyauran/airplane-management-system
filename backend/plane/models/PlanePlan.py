from django.db import models

from ...pilot.models.Pilot import Pilot
from backend.plane.models.Plane import Plane


class PlanePlan(models.Model):
    plane_id = models.ForeignKey(Plane, on_delete=models.CASCADE)
    f_pilot_id = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    s_pilot_id = models.ForeignKey(Pilot, on_delete=models.CASCADE, null=True)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    cords = models.JSONField(default=dict)

    class Meta:
        db_table = 'plane_plan'
        verbose_name = 'Plane Plan'
        verbose_name_plural = 'Plane Plans'

    def __str__(self):
        return self.plane_id
