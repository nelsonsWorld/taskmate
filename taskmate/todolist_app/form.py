from django import forms
from todolist_app.models import TaskList

class TaskForm(forms.ModelForm):
   #What is Meta class?
    class Meta:
        model = TaskList
        fields = ['task', 'done']