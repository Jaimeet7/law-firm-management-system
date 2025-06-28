from django.shortcuts import render,redirect
from btrapp.forms import UserForm,UserProfileForm,UserUpdateForm,UserProfileUpdateForm
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse
from btrapp.models import UserProfile
from django.contrib.auth.decorators import login_required


def registration(request):
    registered = False
    if request.method == "POST":
        form = UserForm(request.POST)
        form1 = UserProfileForm(request.POST,request.FILES) #request.FILES is used to accept multi media data

        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            
            profile = form1.save(commit=False)
            profile.user = user # We are merging 2 models
            profile.save()
            registered = True
    else:
        form = UserForm()
        form1 = UserProfileForm()
    context = {
        'form': form,
        'form1': form1,
        'registered': registered
    }
    return render(request,"registration.html",context)

def userlogin(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('home')
        else:
            return HttpResponse('Invalid credentials, please enter correct username or password')
    return render(request,"login.html",{})

@login_required(login_url='login')
def home(request):
    return render(request,"home.html",{})
@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    return render(request,"profile.html",{})

@login_required(login_url='update')
def update(request):
    if request.method == "POST":
        form  = UserUpdateForm(request.POST, instance = request.user)
        form1 = UserProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.save()

            profile = form1.save()
            profile.user = user
            profile.save()
            return redirect('profile')
    else:
        form  = UserUpdateForm(instance = request.user)
        form1 = UserProfileUpdateForm(instance=request.user.userprofile)
    return render(request,"update.html",{'form':form,'form1':form1})


