from django.shortcuts import render , redirect, get_object_or_404

from django.views.generic import View , UpdateView

from task_app.forms import Taskform

from task_app.models import TaskManager

from django.urls import reverse_lazy

from django.db.models import Q

# Create your views here.

class Add_task(View):

    def get(self,request):

        form=Taskform

        return render(request,'add_task.html',{'form':form})
    
    def post(self,request):

        form=Taskform(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

            task=form.save(commit=False)

            task.user = request.user

            task.save()


        return redirect('home')
    


class Tasklist(View):

    def get (self, request):

        if request.user.is_authenticated:

            task = TaskManager.objects.filter(user=request.user)

            return render(request,'base.html', {'task':task})
        
        return render(request,'base.html')
    
    


class TaskUpdate(UpdateView):

    model = TaskManager

    form_class= Taskform

    template_name = 'update.html'

    success_url = reverse_lazy ('home')


    def get_queryset(self):
        return TaskManager.objects.filter(user=self.request.user)



class Task_delete(View):

    def get( self,request,**kwarges):

        id= kwarges.get('pk')

        task= get_object_or_404(TaskManager, id=id, user=request.user )

        task.delete()

        return redirect('home')
    


class Task_complet(View):

    def get(self, request,**kwargs):

        id= kwargs.get('pk')

        task=get_object_or_404(TaskManager, id=id , user=request.user)

        task.completed = True

        task.save()

        return redirect('home')




class TaskSearchView(View):

    template_name='task_search.html'

    def get(self,request):

        query= request.GET.get('q')

        # filtering all expenses of the logined user

        task= TaskManager.objects.filter(user=request.user)

        # filtering using the given query from thw filtered expence above

        if query:

            task = task.filter(Q(title__icontains = query) | Q(priority__icontains = query))



        return render(request, self.template_name,{'task':task})