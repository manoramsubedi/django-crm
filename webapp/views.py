from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm, AddRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Record


#home
def home(request):
    return render(request, 'webapp/index.html')



#  register
def register(request):
    form = RegisterForm()  #from forms.py

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


#user-logout
def logout(request):

    auth.logout(request)
    return redirect('login')



#dashboard
@login_required(login_url='login')
def dashboard(request):

    my_records = Record.objects.all()
    context = {'records':my_records}

    return render(request, 'webapp/dashboard.html', context)

#add record
@login_required(login_url='login')
def add_record(request):

    form = AddRecordForm()

    if request.method == 'POST':

        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('dashboard')
        
    context={'form':form}
    return render(request, 'webapp/add-record.html', context)











