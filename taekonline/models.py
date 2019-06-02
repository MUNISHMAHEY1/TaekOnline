from django.db import models, connections
import datetime
from django.utils import timezone
import pytz
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal
from phonenumber_field.modelfields import PhoneNumberField

      
class Student(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    date_joined = models.DateTimeField(auto_now=False, auto_now_add=True)
    phone_number = PhoneNumberField()
    email = models.EmailField(blank=False, null=False)
    address_number = models.IntegerField(null=False, blank=False)
    address_street = models.CharField(max_length=200, null=False, blank=False)
    address_complement = models.CharField(max_length=200, null=True, blank=True)
    address_zip_code = models.CharField(max_length=6, null=False, blank=False)
    address_city = models.CharField(max_length=50, null=False, blank=False)
    active = models.BooleanField(default=True)

    @property
    def name(self):
        return ', '.join((self.first_name,self.last_name))

    def __str__(self):
        return self.name


class ContactType(models.Model):
    description = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.description


class StudentContact(models.Model):
    student = models.ForeignKey(to=Student, null=False, blank=False, on_delete=models.CASCADE, related_name='student')
    contact_type = models.ForeignKey(to=ContactType, null=False, blank=True, on_delete=models.PROTECT)
    order = models.IntegerField(null=False, blank=False, default=0)
    contact = models.ForeignKey(to=Student, null=True, blank=True, on_delete=models.CASCADE, related_name='contact')
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = PhoneNumberField(blank=True)

    def __str__(self):
        if self.contact:
            return self.contact.__str__()
        else:
            return ', '.join((self.first_name,self.last_name))