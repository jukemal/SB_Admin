from django.urls import path
from .views import list_meals,sale_predict

urlpatterns = [
    path('list_meals', list_meals, name='predict_list_meals'),
    path('sale_prediction/<int:id>', sale_predict, name='predict_sales')
]
