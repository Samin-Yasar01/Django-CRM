from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect


def home(request):
	# Check to see if logging in
	if request.method == "POST":
		username = request.POST.get("Username")  # Use get() to prevent KeyError
		password = request.POST.get("Password")

		# Authenticate
		user = authenticate(request, username=username, password=password)  # Use lowercase variable names
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In")  # Use 'messages' (plural)
			return redirect('home')
		else:
			messages.error(request, "There Was An Error Logging In, Please Try Again...")  # 'messages.error' is better
			return redirect('home')
	else:
		return render(request, 'home.html', {})
	

def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')



def register_user(request):
	return render(request, 'register.html', {})