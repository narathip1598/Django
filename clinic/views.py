from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import CreateBetLotto
from django.contrib.auth.models import User,auth
from django.contrib import messages

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

def addBet(request):
    numberLotto = request.POST['numberLotto']
    top = request.POST['top']
    down = request.POST['down']
    price = request.POST['price']
    CreateBetLotto.objects.create(numberLotto=numberLotto,top=top,down=down,price=price)
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