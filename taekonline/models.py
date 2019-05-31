from django.db import models, connections
import datetime
from django.utils import timezone
import pytz
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal

      
class Student(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + ', ' + self.last_name