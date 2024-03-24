from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, AddEntryForm, UpdateEntryForm

from  django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import ShipRecords



#homepage
def home(request):
    
    # return HttpResponse('Hello World')

    return render(request, 'myCRMApp/index.html')



#registerpage - to register a user
def register(request):
    
    form = CreateUserForm()
    
    #check request
    if request.method == "POST":

        form = CreateUserForm(request.POST)
    
        if form.is_valid():

            form.save()

            # for redirecting user after registering
            return redirect('login')
    
    context = {'formRegister' : form}
    
    return render(request, 'myCRMApp/register.html', context=context)



#registerpage - to register a user
def login(request):
    form  = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password  = request.POST.get('password')

            user =  authenticate(request, username=username, password=password)

            if user is not None:
                
                auth.login(request, user)

                #after login in redirect user to dashboard
                return redirect('dashboard')


    context = {'formLogin': form}
    return render(request, 'myCRMApp/login.html', context=context)



#dashboardpage -  to make user see dashboards
@login_required(login_url='login')
def dashboard(request):

    myrecords = ShipRecords.objects.all()

    context =  {'records': myrecords}

    return render(request, 'myCRMApp/dashboard.html', context=context)



#createrecord - to add record
@login_required(login_url='login')
def create_entry(request):

    form =  AddEntryForm()

    if request.method == 'POST':

        form = AddEntryForm(request.POST)

        if form.is_valid():
            
            form.save()

            return redirect('dashboard')


    context = {'formAdd': form}

    return render(request, 'myCRMApp/create_entry.html', context=context)



#updaterecord - to add record
@login_required(login_url='login')
def update_entry(request, pk):

    record = ShipRecords.objects.get(id=pk)
    
    form = UpdateEntryForm(instance=record)

    if request.method == 'POST':
        
        form = UpdateEntryForm(request.POST, instance=record)

        if form.is_valid():
            
            form.save()

            return redirect('dashboard')
        

    context = {'formUpdate': form}

    return render(request, 'myCRMApp/update_entry.html', context=context)



#viewsinglerecord - to view record
@login_required(login_url='login')
def view_entry(request, pk):

    all_records = ShipRecords.objects.get(id=pk)

    context = {'record': all_records}

    return render(request, 'myCRMApp/view_entry.html', context=context)



#deleterecord - to delete a recod
@login_required(login_url='login')
def delete_entry(request, pk):

    record =  ShipRecords.objects.get(id=pk)

    record.delete()

    return redirect('dashboard')



#logout page - to make user logout
def logout(request):

    auth.logout(request)

    return redirect('')