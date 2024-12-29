from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from . forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# def indexr(request):
#     return HttpResponse("Hello world")

# def About(request):
#     return HttpResponse("Welcome to website")

# def index(request):
#     return render(request,'index.html')

# def contactus(request):
#     return render(request,'contactus.html')

# def about(request):
#     return render(request,'about.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contactus.html')

def predict(request):
    return render(request,'predictform.html')

def result(request):
    if request.method == 'POST':
        glucose = request.POST['Glucose']
        blood_p = request.POST['bp']
        skin_th = request.POST['skinthic']
        insulin = request.POST['Insulin']
        bmi = request.POST['bmi']
        dpf = request.POST['Pedigreefun']
        age = request.POST['Age']

        lis = [glucose,blood_p,skin_th,insulin,bmi,dpf,age]
        print(lis)

        #Training model
        from joblib import load 
        model = load('D:\web dev\Django\myproject\model.joblib')

        #make prediction
        result = model.predict([lis])
        print(result)

        if result[0]==0:
            print("No")
            value='Negative'

        else:
            print('Yes')
            value='Positive'
    
    return render(request,'result.html',{
        'ans': value,
        'title' : 'Predict',
    })

login_required(login_url='lohin_view')


def register(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request,user)
            return redirect('login_view')
    else:
        form = RegisterForm() 
    return render(request, 'register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('predict')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout1(request):
    logout(request)
    messages.success(request,'Logged out successfully')
    return redirect('/')




