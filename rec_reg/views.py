from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
# Create your views here.

@login_required(login_url='login')

def HomePage(request):
    return render (request, "index.html")

def RecReg(request):
    global name
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        cname=request.POST.get('cname')
        password=request.POST.get('password')
        my_user = User.objects.create_user(username = name, email = email, first_name = cname, password =  password, )
        my_user.save()
        return redirect('Login')
    return render (request, 'rec_reg.html')

def JobPage(request):
    context = {
        "name" : name
    }
    return render (request, 'jobs.html', context)

def RecLogin(request):
    if request.method == "POST" :
        in_name = request.POST.get('name')
        in_password = request.POST.get('password')
        user = authenticate(request, username=in_name, password = in_password)
        if user is not None:
            login(request,user)
            return redirect('Jobs')
        else:
            return HttpResponse ("Wrong Password")
    return render(request, 'rec_login.html' )

def LogoutPage (request):
    logout(request)
    return redirect('Login')