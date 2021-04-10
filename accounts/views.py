from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm
from .forms import intrestForm
#from .filters import OrderFilter

def registerPage(request):
  form = CreateUserForm()

  if request.method == 'POST':
        form = CreateUserForm(request.POST) 
        if form.is_valid():
         form.save()
         user = form.cleaned_data.get('username')
         messages.success(request, 'Account '+ user + 'has been created')


         return redirect('login')
 

  context = {'form':form}
  return render(request, 'accounts/register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect!')
        


    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
  return render(request, 'accounts/dashboard.html', {})

def intrestForm_view(request):
  form = intrestForm(request.POST)
  if form.is_valid():
      form.save()

      return redirect('login')
  context = { 'form': form}
  return render(request,'accounts/quiz.html',context)
   
@login_required
def profile(request):
  return render(request, 'accounts/profile.html',{})