from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import CreateBetLotto
from django.contrib.auth.models import User


def hello(request):
    data=CreateBetLotto.objects.all()
    return render(request,'index.html',{'CreateBetLotto':data})

def page1(request):
    return render(request,'page1.html',
    {
        
    })

def form(request):
    return render(request,'form.html')

def addLotto(request):
    numberLotto=request.POST['numberLotto']
    top=request.POST['top']
    down=request.POST['down']
    price=request.POST['price']
    return render(request,'result.html',{'numberLotto':numberLotto,'top':top,'down':down,'price':price})


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
            print("Username นี้ถูกใช้ไปแล้ว")
            return redirect('/register')
        elif User.objects.filter(email=email).exists():
            print("Email นี้ถูกใช้ลงทะเบียนไปแล้ว")
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
        return redirect('/register')