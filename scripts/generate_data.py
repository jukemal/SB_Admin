import pandas as pd
import datetime
import numpy as np
from pathlib import Path
import os
import random

from django.contrib.auth.models import User
from accounts.models import Customer, Meal, Order

CURRENT_DIR = Path(__file__).resolve(strict=True).parent

FILE_NAME = 'order_data.csv'

np.random.seed(101)

DAYS = 100

MIN_MEAL_COUNT = 40
MAX_MEAL_COUNT = 60

meals = {
    1: {
        "name": "Rice and Curry Vegetable",
        "price": 170,
    },
    2: {
        "name": "Rice and Curry Egg",
        "price": 190,
    },
    3: {
        "name": "Rice and Curry Fish",
        "price": 200,
    },
    4: {
        "name": "Rice and Curry Chicken",
        "price": 200,
    },
    5: {
        "name": "Egg Rice",
        "price": 200,
    },
    6: {
        "name": "Chicken Rice",
        "price": 320,
    },
    7: {
        "name": "Egg Kottu",
        "price": 200,
    },
    8: {
        "name": "Chicken Kottu",
        "price": 280,
    },
    9: {
        "name": "Egg Biriyani",
        "price": 250,
    },
    10: {
        "name": "Chicken Biriyani",
        "price": 360,
    },
}

customers = []
meal_list = []


def run(*args):
    df = pd.read_csv(os.path.join(
        CURRENT_DIR, FILE_NAME), parse_dates=['Date'])
    print(df.info())
    print(df.head())

    user, _ = User.objects.get_or_create(username="user")

    user.set_password('123456')

    user.save()

    print(user)

    for i in range(5):
        cus = Customer(
            name=f'Customer {i+1}',
            contact_number=f'01234678{i+1}',
            email=f'customer{i+1}@customer.com',
            address=f'{i+1} Lane, Colombo.',
            user=user,
        )

        customers.append(cus)

        print(cus)

        cus.save()

    for i in range(len(meals)):
        me = Meal(
            meal_name=meals[i+1]['name'],
            price=meals[i+1]['price'],
            user=user,
        )

        meal_list.append(me)

        print(me)

        me.save()

    for index, row in df.iterrows():
        print(index)

        order = Order(
            customer=random.choice(customers),
            meal=meal_list[row['Index']-1],
            qty=row['Quantity'],
            status='Delivered',
            user=user,
            datetime=row['Date'].to_pydatetime(),
        )

        print(order)

        order.save()
