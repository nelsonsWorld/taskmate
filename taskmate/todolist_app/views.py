from django.shortcuts import render
from django.http import HttpResponse

def todolist(request):
    return render(request,'todolist.html', {"welcome_text":"Yeahh!!!!"})
    #return HttpResponse("Welcome To Task Page")


def contact(request):
    context = {
        'welcome_text':"Welcome Contact Page.",
    }
    return render(request,'contact.html', context)

def about(request):
    context = {
        'welcome_text':"Welcome to About Page.",
    }
    return render(request, 'about.html', context)