from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required


#home
def home(request):
    #return HttpResponse("HELLO ALL!")
    return render(request, 'webapp/index.html')

# def about(requst):
#     return render("THIS IS ABOUT SECTION")


#  register
def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')
    context = {'form':form}
    return render(request, 'webapp/register.html', context)
    

#login
def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form=LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)

                return redirect('dashboard')

    context={'form':form}
    return render(request, 'webapp/login.html', context)


#dashboard
@login_required(login_url='login')
def dashboard(request):

    return render(request, 'webapp/dashboard.html')

#user-logout
def logout(request):

    auth.logout(request)
    return redirect('login')










