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
    address_number = models.IntegerField(verbose_name="number", null=False, blank=False)
    address_street = models.CharField(verbose_name="street", max_length=200, null=False, blank=False)
    address_complement = models.CharField(max_length=200, null=True, blank=True)
    address_zip_code = models.CharField(max_length=6, null=False, blank=False)
    address_city = models.CharField(max_length=50, null=False, blank=False)
    active = models.BooleanField(default=True)
    
    @property
    def name(self):
        return ', '.join((self.first_name,self.last_name))

    @property
    def rank(self):
        if self.rankhistory_set.count() > 0:
            return self.rankhistory_set.all().order_by('-rank__order')[0].rank.description
        return None

    def __str__(self):
        return self.name


class ContactType(models.Model):
    description = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.description


class StudentContact(models.Model):
    student = models.ForeignKey(to=Student, null=False, blank=False, on_delete=models.CASCADE, related_name='student')
    contact_type = models.ForeignKey(to=ContactType, null=False, blank=True, on_delete=models.PROTECT)
    #order = models.IntegerField(null=False, blank=False, default=0)
    contact = models.ForeignKey(to=Student, null=True, blank=True, on_delete=models.CASCADE, related_name='contact')
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = PhoneNumberField(blank=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        if self.contact:
            return self.contact.__str__()
        else:
            return ', '.join((self.first_name,self.last_name))

class Rank(models.Model):
    description = models.CharField(max_length=100, null=False, blank=False)
    order = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.description

class RankHistory(models.Model):
    rank = models.ForeignKey(Rank, null=False, blank=False, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, null=False, blank=False, on_delete=models.PROTECT)
    exam_date = models.DateTimeField(null=False, blank=False)


class ClassCathegory(models.Model):
    description = models.CharField(max_length=100, null=False, blank=False)
    color = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.description


class ClassAgenda(models.Model):
    cathegory = models.ForeignKey(ClassCathegory, null=True, blank=True, on_delete=models.SET_NULL)
    start_time = models.TimeField()
    end_time = models.TimeField()
    sunday = models.BooleanField(default=False)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)


class Attendance(models.Model):
    student = models.ForeignKey(Student, null=False, blank=False, on_delete=models.PROTECT)
    class_date = models.DateTimeField(null=False, blank=False)


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.CharField(max_length=200, null=False, blank=False)
    cost_price = models.DecimalField(null=False, blank=False, max_digits=18, decimal_places=2, default=0)
    selling_price = models.DecimalField(null=False, blank=False, max_digits=18, decimal_places=2)
    quantity = models.IntegerField(null=False, blank=False, default=1)
    keep_inventory = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Income(models.Model):
    income_date = models.DateField(null=False, blank=False)
    income_time = models.TimeField(null=False, blank=False)
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE)

class IncomeProduct(models.Model):
    income = models.ForeignKey(Income, null=False, blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=1)
    profit = models.DecimalField(null=True, blank=True, max_digits=18, decimal_places=2)

    def __str__(self):
        return ' '.join((str(self.income.id), self.product.name))

    '''
    def save(self, *args, **kwargs):
        self.profit = self.quantity * (self.product.selling_price - self.product.cost_price)
        super(Model, self).save(*args, **kwargs)
        #super().save(*args, **kwargs)
    '''








