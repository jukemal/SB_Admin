from django.contrib import admin

# Register your models here.
from .models import Order
from .models import Meal
from .models import Tag
from .models import Customer

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Meal)
admin.site.register(Tag)