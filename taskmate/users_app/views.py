from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm #Class names use capitals and functions use lowercase.
# from django.http import HttpResponse
# Create your views here.


def register(request):
    register_form = UserCreationForm()
  #  return HttpResponse("Users_app working!")
    return render(request, 'register.html', {'register_form': register_form})
