from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.models import User


class Customer(models.Model):
		name = models.CharField(max_length=200, null=True)
		contact_number = models.CharField(max_length=200, null=True)
		email = models.CharField(max_length=200, null=True)
		Address = models.CharField(max_length=200, null=True)
		user = models.ForeignKey(User,on_delete=models.CASCADE)


		def __str__(self):            
			return self.name        

class Tag(models.Model):
		name = models.CharField(max_length=200, null=True)

		def __str__(self):
			return self.name 
			

class Meal(models.Model):
		meal_name=models.CharField(max_length=200, null=True)
		price = models.FloatField(null=True)		
		description = models.CharField(max_length=200, null=True)
		tags = models.ManyToManyField(Tag)
		user = models.ForeignKey(User,on_delete=models.CASCADE)
	
		def __str__(self):                                      
			return self.meal_name                                
                                                   
class Order(models.Model):                                
		STATUS = (
				('Pending', 'Pending'),
				('Out for delivery', 'Out for delivery'),
				('Delivered', 'Delivered'),
				)

		customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
		meal = models.ForeignKey(Meal, null=True, on_delete= models.SET_NULL)
		date_created = models.DateTimeField(auto_now_add=True, null=True)
		qty=models.IntegerField(null=True)
		status = models.CharField(max_length=200, null=True, choices=STATUS)
		user = models.ForeignKey(User,on_delete=models.CASCADE)