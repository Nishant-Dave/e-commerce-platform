from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile



def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username = email).exists():
            messages.warning(request, "This email is taken")
            return HttpResponseRedirect(request.path_info)

        user_obj = User.objects.create(
            first_name = first_name,
            last_name = last_name, 
            email = email, 
            username = email
            )
        user_obj.set_password(password)
        user_obj.save()
        
        messages.success(request, 'Email sent. Check your inbox.')
        return redirect('login')

    return render(request, 'accounts/register.html')


def activate_email(request, email_token):
    try:
        user = Userprofile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()

    except Exception as e:
        return HttpResponse('Invalid Email token')

    return redirect('/')



def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if not User.objects.filter(username = email).exists():
            messages.warning(request, "Account not found")
            return HttpResponseRedirect(request.path_info)

        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, "Your account is not varified.")
            return HttpResponseRedirect(request.path_info)


        user_obj= authenticate(username = email, password = password)
        if user_obj:
            login(request, user_obj)
            return redirect('/')
        
        messages.warning(request, 'Invalid credentials')
        return redirect('login')




    return render(request, 'accounts/login.html')
