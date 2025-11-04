from django.shortcuts import render ,redirect

from django.views.generic import View

from user_app.forms import Userregister

from user_app.models import User

from django.contrib.auth import authenticate , login, logout

# Create your views here.

class Register(View):

    def get (self,request):

        form=Userregister()

        return render(request,'register.html',{'form':form})
    

    def post(self,request):

        username=request.POST.get('username')

        email=request.POST.get('email')

        password=request.POST.get('password')


        User.objects.create_user(username=username,
                                 email=email,
                                 password=password)


        form=Userregister()

        return redirect('home')
    



class LoginView(View):

    def get(self, request):

        return render (request,'login.html')


    def post(self,request):

        username=request.POST.get('username')

        password=request.POST.get('password')


        user=authenticate(request,username=username, password=password)


        if user:

            login(request,user)


            return redirect('home')
        
        form=Userregister()
        
        return render(request,'register.html',{'form':form} )
    


class Logoutview(View):

    def get (self, request):

        logout(request)

        return redirect('login')


