from django.shortcuts import render,redirect

from blog.models import category,blog
from blog_main.forms import RegisterForm
from extra.models import About
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth



def home(request):
    # categories=category.objects.all()
    featured_post=blog.objects.filter(is_featured=True,status='Published').order_by('-updated_at')
    post=blog.objects.filter(is_featured=False,status='Published').order_by('-updated_at')

    #fetch about us
    try:
        about=About.objects.get()
    except:
        about=None

    context={
        # 'categories':categories,
        'featured_post':featured_post,
        'post':post,
        'about':about,
    }
    return render(request, 'home.html',context)

def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }

    return render(request, 'register.html',context)

def login(request):
    if request.method=='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
    form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('home')