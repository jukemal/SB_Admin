from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.models import User


class Customer(models.Model):
    name = models.CharField(max_length=200, unique=True)
    contact_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Customer : "+self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Meal(models.Model):
    meal_name = models.CharField(max_length=200, unique=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=200, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Meal : "+self.meal_name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True)
    qty = models.IntegerField()
    datetime = models.DateTimeField()
    status = models.CharField(max_length=200, choices=STATUS)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Order : "+self.meal.meal_name+", Quantity : "+str(self.qty)
