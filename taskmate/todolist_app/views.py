# Don't forget to import redirect!
from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.form import TaskForm 
from django.contrib import messages

def todolist(request):

    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        # import the messages method from the django.contrib module/library
        messages.success(request,("New Task Added!"))
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.all
        return render(request, 'todolist.html', {'all_tasks': all_tasks})  

    # context = {
    #     'welcome_text':"Welcome Todolist Page.",
    # }

     # return render(request, 'todolist.html', context)  
    # return render(request,'todolist.html', {"welcome_text":"Yeahh!!!!"})
    # #return HttpResponse("Welcome To Task Page")


def contact(request):
    context = {
        'contact_text':"Welcome Contact Page.",
    }
    return render(request,'contact.html', context)

def about(request):
    context = {
        'about_text':"Welcome to About Page.",
    }
    return render(request, 'about.html', context)