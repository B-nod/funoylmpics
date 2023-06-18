import contextvars
from multiprocessing import context
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.cache import never_cache
from .decorators import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@never_cache
@not_logged_in_required
def login_user(request):
    form = LoginForm()
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data.get('username'),
                password = form.cleaned_data.get('password')
            )
            
            if user:
                login(request,user)
                return redirect('home')
            else:
                messages.warning(request,"Wrong credentials")
            
    
    context = {
        "form":form
    }
    return render(request, 'login.html',context)


def logout_user(request):
    logout(request)
    return redirect('login')


@never_cache
@not_logged_in_required
def register_user(request):
    form = UserRegistrationForm()
    
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            messages.success(request,"Registraion Sucessful")
            return redirect('login')
        
            
            
    context = {
        "form":form
    }
    return render(request, 'registration.html',context)



@login_required(login_url = 'login')
def profilechange(request):
    account = get_object_or_404(User, pk = request.user.pk )
    form = UserProfileUpdateForm(instance = account)
    
    if request.method == "POST":
        if request.user.pk != account.pk:
            return redirect('home')
        form = UserProfileUpdateForm(request.POST, instance = account)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile has been updated sucessfully")
            return redirect('profile')
        
        
    context = {
        "account":account
    }
    return render(request, 'profile.html',context)


@login_required
def change_profile_picture(request):
    if request.method == "POST":
        form = ProfilePictureUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['profile_image']
            user = get_object_or_404(User, pk = request.user.pk)
            
            if request.user.pk != user.pk:
                return redirect('home')
            
            user.profile_image = image
            user.save()
            messages.success(request,"Profile updated successfully")
            
            
    return redirect('profile')


@login_required(login_url = 'login')
def profile(request):
    account = get_object_or_404(User, pk = request.user.pk )
                
    context = {
        "account":account
    }
    return render(request, 'basicprofile.html',context)


@login_required(login_url = 'login')
def change_password(request):
    account = get_object_or_404(User, pk = request.user.pk )
    form = UserProfileUpdateForm(instance = account)
    
    if request.method == "POST":
        if request.user.pk != account.pk:
            return redirect('home')
        form = UserProfileUpdateForm(request.POST, instance = account)
        if form.is_valid():
            form.save()
            messages.success(request,"Password has been updated sucessfully")
            return redirect('profile')
        
        
    context = {
        "account":account
    }
    return render(request, 'change_password.html',context)




    



# def forgot_password(request):
#     if request.method == "POST":
#         # form = LoginForm(request.POST)
#         # if form.is_valid():
#         username = request.POST.get('username')
            
#         if User.objects.filter(username = username).first():
#             return redirect('password_reset_done')
#         else:
#             messages.warning(request,"No Username Found. Please Type the correct username.")
            
#     return render(request, 'forgot_Password.html')


# @never_cache
# @not_logged_in_required

# def forgot_password_done(request):
#     # form = LoginForm()

#     return render(request, 'password_reset.html')


    
    
    
            
    




