from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .models import *


class RegisterView(View):
    def get(self,request):
        DAVLATLAR = (
            'Uzbekistan',
            'Russia',
            'Armenia',
            'Tajikistan',
            'Kazakhstan',
            'Kyrgzstan',
            'Azerbayjan',
            'Moldova',
            'Latviya',
            'Turkmenistan',
        )
        content = {
            'davlatlar':DAVLATLAR
        }
        return render(request,'page-user-register.html',content)

    def post(self,request):
        if request.POST.get('password') == request.POST.get('password2'):
            u = User.objects.create_user(
                username= request.POST.get('username'),
                password= request.POST.get('password'),
                first_name = request.POST.get('first'),
                last_name = request.POST.get('last'),
            )
            Account.objects.create(
                jins = Account.objects.get(jins=request.POST.get('jins')),
                shahar = request.POST.get('shahar'),
                davlat = Account.objects.get(davlat=request.POST.get('davlat')),
                user = u
            )
            return redirect('login')

class LoginView(View):
    def get(self,request):
        return render(request,'page-user-login.html')

    def post(self,request):
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user is None:
            return redirect('login')
        login(request,user)
        return redirect('home')


class LogoutView(View):
    def get(self,request):
        logout(User)
        return redirect('/login/')


