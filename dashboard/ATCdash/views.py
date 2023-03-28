from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages


@login_required(login_url='login')
def dashboard(request):
    # messages.success(request, 'login Sucessfully')
    return render(request, 'main.html')


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        log = authenticate(request, username=username, password=password)

        if log is not None:
            login(request, log)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'index.html')


def log_out(request):
    messages.success(request, 'logout Successfully')
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        return redirect('dashboard')