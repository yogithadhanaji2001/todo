from django import forms

from task_app.models import TaskManager

class Taskform(forms.ModelForm):

    class Meta:

        model = TaskManager

        fields =['title', 'description','priority' ]
