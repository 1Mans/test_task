from django.conf import settings
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Rank(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    HIGH = "Высшее"
    MEDIUM = "Средне-специальное"
    SCHOOL = "Среднее"
    YEAR_IN_SCHOOL_CHOICES = [
        (HIGH, "Высшее"),
        (MEDIUM, "Средне-специальное"),
        (SCHOOL, "Среднее"),
    ]
    year_in_school = models.CharField(
        max_length=20,
        choices=YEAR_IN_SCHOOL_CHOICES,
    )
    years_worked = models.IntegerField()
    dob = models.DateField()
    date_accepted = models.DateField()
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=False
    )
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.first_name
