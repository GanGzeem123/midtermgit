from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,'base.html')

def login(request):
    return render(request,'login.html')

def reportrequest(request):
    return render(request,'reportrequest.html')

def request(request):
    return render(request,'request.html')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('/list')
        else:
            messages.error(request, 'Login failed. Please check your credentials.')
            pass
    return render(request, 'login.html')

