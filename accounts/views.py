from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
from .forms import MealForm
from .forms import CustomerForm, CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for' + user)

                return redirect('log')

        context = {'register_form': form}
        return render(request, 'register.html', context)


def logUsers(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('log')


@login_required(login_url='log')
def home(request):
    customers = Customer.objects.filter(user=request.user)
    orders = Order.objects.filter(user=request.user)

    total_customers = customers.count()
    total_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers,
               'order_count': total_orders, 'total_deliverd': delivered,
               'total_pending': pending}

    return render(request, 'dashboard.html', context)


@login_required(login_url='log')
def customerList(request):
    customers = Customer.objects.filter(user=request.user)
    #customers = Customer.objects.filter(user=request.user)
    contex = {'customers': customers, }
    return render(request, 'customerList.html', contex)


@login_required(login_url='log')
def meals(request):
    meals = Meal.objects.filter(user=request.user)
    return render(request, 'meals.html', {'meals': meals})


@login_required(login_url='log')
def addMeal(request):
    meal_form = MealForm()
    meal_form = MealForm(request.POST or None)
    if meal_form.is_valid():
        form = meal_form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('/')
    context = {'add_new_meal_form': meal_form}
    return render(request, 'addMeals.html', context)


@login_required(login_url='log')
def customerDetails(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()  # Returns all orders related to customer
    order_count = orders.count()

    context = {'customer': customer,
               'view_customer_oders': orders, 'order_count': order_count}
    return render(request, 'customer.html', context)


@login_required(login_url='log')
def createOrder(request):
    form = OrderForm()
    form = OrderForm(request.POST or None)
    if (form.is_valid()):
        new_form = form.save(commit=False)
        new_form.user = request.user
        new_form.save()
        return redirect('/')
    context = {'order_form': form}
    return render(request, 'order_form.html', context)


@login_required(login_url='log')
def createCustomer(request):
    new_form = CustomerForm()
    new_form = CustomerForm(request.POST or None)
    if new_form.is_valid():
        form = new_form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('/')
    context = {'customer_form': new_form}
    return render(request, 'add_customer.html', context)

    context = {'customer_form': new_form}
    return render(request, 'add_customer.html', context)


@login_required(login_url='log')
def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'new_form': form}
    return render(request, 'order_form.html', context)


@login_required(login_url='log')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'order_delete.html', context)
