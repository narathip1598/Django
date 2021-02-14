from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import CreateBetLotto
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .form import name
from django.utils.datastructures import MultiValueDictKeyError

def hello(request):
    data=CreateBetLotto.objects.all()
    return render(request,'index.html',{'CreateBetLotto':data})

def page1(request):
    return render(request,'page1.html',
    {
        
    })

def form(request):
    return render(request,'form.html')

def loginForm(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def addAccount(request):
    username=request.POST['username']
    firstName=request.POST['firstName']
    lastName=request.POST['lastName']
    email=request.POST['email']
    password=request.POST['password']
    repassword=request.POST['repassword']
    if password==repassword :
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username นี้ถูกใช้ไปแล้ว')
            return redirect('/register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email นี้ถูกใช้ไปแล้ว')
            return redirect('/register')
        else : 
            user=User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=firstName,
            last_name=lastName
            )
            user.save()
            return redirect('/')
    else : 
        messages.info(request,'password ไม่ตรงกัน')
        return redirect('/register')

def addBet(request) :
    numberLotto=request.POST['numberLotto']
    top=request.POST['top']
    down=request.POST['down']
    price=request.POST['price']
    bet=CreateBetLotto.objects.create(
        numberLotto=numberLotto,
        top=top,
        down=down,
        price=price
        )
    bet.save()
    return redirect('/')

def login(request):
    username=request.POST['username']
    password=request.POST['password']
    user=auth.authenticate(username=username,password=password)
    if user is not None :
        auth.login(request,user)
        return redirect('/')
    else :
        messages.info(request,'ข้อมูลไม่ถูกต้อง')
        return redirect('/loginForm')

def logout(request):
    auth.logout(request)
    return redirect('/')

def get_name(request):
    if request.method == 'POST':
        form = name(request.POST)
        if form.is_valid():
            numberLotto=request.POST['numberLotto']
            try:
                top = request.POST['top']
                down = request.POST['down']
                if top == 'on' and down == 'on':
                    top = 'True'
                    down = 'True'
            except MultiValueDictKeyError:
                top=False
                down=False
                if top == 'on':
                        top='True'
                        down='False'
                elif down == 'on':
                    top='False'
                    down='True'
            price=request.POST['price']
            CreateBetLotto.objects.create(
                numberLotto=numberLotto,
                top=top,
                down=down,
                price=price
            )
            return HttpResponseRedirect('/')
    else: 
        form = name()
    return render(request,'name.html',{'form':form})