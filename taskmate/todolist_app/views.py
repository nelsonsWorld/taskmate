from django.shortcuts import render
from django.http import HttpResponse

def todolist(request):
    return render(request,'todolist.html', {})
    #return HttpResponse("Welcome To Task Page")


def contact(request):
    return render(request,'contact.html', {})

def about(request):
    return render(request, 'about.html', {})