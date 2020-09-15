from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
import datetime
import numpy as np

from accounts.models import Meal, Order
from .predict import predict_sales


@login_required(login_url='log')
def list_meals(request):
    meals = Meal.objects.all()

    context = {
        'meals': meals
    }

    return render(request, 'list_meals.html', context)


@login_required(login_url='log')
def sale_predict(request, id):
    meal = get_object_or_404(Meal, pk=id)

    orders = Order.objects.filter(meal__id=id)

    real_list, predicted_list, _ = predict_sales(meal, orders)

    real = []

    for i in real_list:
        real.append({
            'x': i['date'].strftime('%Y-%m-%d'),
            'y': i['count']
        })

    predicted = []

    for i in predicted_list:
        predicted.append({
            'x': i['date'].strftime('%Y-%m-%d'),
            'y': i['count']
        })

    context = {
        'real': real,
        'predicted': predicted
    }

    return render(request, 'sale_prediction.html', context)
