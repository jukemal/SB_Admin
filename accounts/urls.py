from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.logUsers, name="log"),
    path('signup/', views.signup,name="register"),
    path('logout/', views.logoutUser,name="logout"),
    path('meals/',views.meals, name="goto_foods_page"),
    path('add_meals',views.addMeal,name="add_new_meal"),
    path('customerList/',views.customerList, name="customer_list_page"),
    path('customer/<str:pk_test>/', views.customerDetails, name="customer_info"),  
    path('create_order/', views.createOrder, name="create_new_order"),
    path('new_customer/', views.createCustomer, name="new_customer"),
    path('create_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

]