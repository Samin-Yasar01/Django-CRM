from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm  # Fixed typo 'froms' -> 'forms'
from .models import Record
from django.shortcuts import get_object_or_404


def home(request):
    records = Record.objects.all()

    # Check to see if logging in
    if request.method == "POST":
        username = request.POST.get("Username")  # Use get() to prevent KeyError
        password = request.POST.get("Password")

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In")
            return redirect('home')
        else:
            messages.error(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered")
            return redirect('home')
    else:
        form = SignUpForm()  # Moved outside the POST check

    return render(request, 'register.html', {'form': form})  # Ensuring it renders properly




def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look up record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.error(request, "You need to be logged in to view this page.")
        return redirect('home')



def delete_record(request, pk):
    if request.user.is_authenticated:
        record = get_object_or_404(Record, id=pk)
        record.delete()
        messages.success(request, "Record deleted successfully.")
        return redirect('home')
    else:
        messages.error(request, "YOU MUST BE LOGGED IN TO DO THAT.")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record added....")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "YOU MUST BE LOGGED IN TO DO THAT.....")
        return redirect('home')
