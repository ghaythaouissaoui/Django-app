from django.shortcuts import render, redirect
from django.views import View
import json
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from .decorators import unauthenticated_user, allowed_users
from django.contrib import messages
from .forms import CreateUserForm, UpdateUserForm
from django.contrib.auth.decorators import login_required
# Create your views here. 
from django.shortcuts import get_object_or_404, redirect
from .models import users


def RegisterPage(request):
    form = CreateUserForm()

    # Get the queryset of users
    users = User.objects.all()  # Change this query according to your needs

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            print("User saved successfully")
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('register')
        else:
            print("Form is not valid:", form.errors)

    context = {
        'form': form,
        'users': users  # Pass the users queryset to the template context
    }
    return render(request, 'authentication/register.html', context)
# views.py

def update_user(request, user_id):
    user_to_update = get_object_or_404(User, id=user_id)
    form = UpdateUserForm(instance=user_to_update)
    
 
    
    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = UpdateUserForm(request.POST, instance=user_to_update)
        if form.is_valid():
            # If the form data is valid, save the updated user data
            form.save()
            # Redirect to a success page or any other desired URL
            return redirect('register')  # Change 'register' to your desired URL name

    # Render the registration template with the form and user data
    context = {'form': form, 'user': user_to_update}
    return render(request, 'authentication/register.html', context)

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('register')

def logoutUser(request):
    logout(request)
    return redirect('login')



@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')

       user = authenticate(request, username=username, password=password)
    
       if user is not None:
        login(request, user)
        return redirect('base')
       
    context={}
    return render(request,'authentication/login.html', context)

@login_required
def home(request):
    if request.user.groups.filter(name='directeur').exists():
        return render(request, 'authentication/base_user.html')
    elif request.user.groups.filter(name='admin').exists():
        return render(request, 'authentication/base.html')

