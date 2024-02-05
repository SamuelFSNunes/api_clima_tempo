from django.shortcuts import render
from .models.ModelUser import ModelUser
# Create your views here.

def home(request):
  return render(request, 'home/home.html')

def users(request):
  data = {}
  data['users'] = ModelUser.objects.all()
  return render(request, 'users/users.html', data)

def login(request):
  return render(request,'login.html')