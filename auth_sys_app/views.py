from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup_view(request):
    context={}
    if request.method == 'POST':
        un=request.POST.get('ue')
        em=request.POST.get('em')
        pw=request.POST.get('pw')
        cpw=request.POST.get('pw2')
        if pw==cpw:
            if User.objects.filter(username=un).exists():#Ensures that no user is registered with same UN
                context['message']="Username already exists"
            else:
                User.objects.create_user(username=un,email=em,password=pw)
                return redirect('signin')#after signup redirecting to signin
        else:
            context['message']="Password not matching"
    return render(request, 'signup.html',context)
def signin_view(request):
    if request.user.is_authenticated:#check if user is already login 
        return redirect('home')#if alredy redirect to home (without login we cant let user to view the home page at any cost)
    context={}
    if request.method=='POST':
        un=request.POST.get('ue')
        pw=request.POST.get('pw')
        user=authenticate(request,username=un,password=pw)#an inbult authentication function  which returns a object (cauz we cannot directly check the passwords whicvh encripted directle '==' like this.)
        if user is not None:#if tht function didnt got the mathing record it will return None
            login(request,user)#after authentication if the credentials are correct we are going to use an inbuilt function login which is going to store credentials in browser session storage .
            return redirect('home')#after login no need to stick up on login page r8!
        else:
            context['message']='Invalid credentials!!'#if user not matched by authenticate functions we are going to add a message in a context to return
    return render(request, 'signin.html',context)    #if it is  a get request directly render the page
# @login_required
def signout_view(request):
    logout(request)# deleting un and ps in  the session storage 
    return redirect('signin')#redirect to login page