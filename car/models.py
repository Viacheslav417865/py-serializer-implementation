from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Car(models.Model):
    manufacturer = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    horse_powers = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(2000), MinValueValidator(0)]
    )
    is_broken = models.BooleanField()
    problem_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.manufacturer}, {self.model}"
