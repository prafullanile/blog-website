from django.shortcuts import render,redirect,get_object_or_404

from blog.models import category, blog
from django.contrib.auth.decorators import login_required

from dashboards.forms import CategoryForm, BlogPostForm, AddUserForm,EditUserForm
from blog.models import category, blog
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from .forms import AddUserForm

# Create your views here.
@login_required(login_url='/login')
def dashboard(request):
    category_count=category.objects.all().count()
    blogs_count=blog.objects.all().count()
    context={
        'category_count':category_count,
        'blogs_count':blogs_count,
    }
    return render(request,'dashboard/dashboard.html',context)

def categories(request):
    return render(request,'dashboard/categories.html')

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form':form,
    }
    return render(request,'dashboard/add_category.html',context)

def edit_category(request, pk):
    category_obj = get_object_or_404(category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category_obj)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form=CategoryForm(instance=category_obj)
    context={
        'form':form,
        'category_obj':category_obj,
    }
    return render(request,'dashboard/edit_category.html',context)

def delete_category(request, pk):
    category_obj = get_object_or_404(category, pk=pk)
    category_obj.delete()
    return redirect('categories')

def posts(request):
    posts = blog.objects.all()
    context = {
        'posts':posts,
    }

    return render(request,'dashboard/posts.html',context)

def add_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)#temporary saving the form
            post.author = request.user
            post.save()
            title=form.cleaned_data['title']
            post.slug=slugify(title) + '-' + str(post.id)
            post.save()

            return redirect('posts')
    form=BlogPostForm()
    context={
        'form':form,
    }
    return render(request,'dashboard/add_post.html',context)

def edit_post(request,pk):
    post = get_object_or_404(blog, pk=pk)
    if request.method == "POST":
        form = BlogPostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            title=form.cleaned_data['title']
            post.slug=slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
    form = BlogPostForm(instance=post)
    context = {
        'form':form,
        'post':post,
    }
    return render(request,'dashboard/edit_post.html',context)

def delete_post(request,pk):
    post = get_object_or_404(blog, pk=pk)
    post.delete()
    return redirect('posts')

#users

def users(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request,'dashboard/users.html',context)

def add_user(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    form=AddUserForm()

    context={
        'form':form,
    }

    return render(request,'dashboard/add_user.html',context)

def edit_user(request,pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = EditUserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = EditUserForm(instance=user)
    context={
        'form':form,
    }

    return render(request,'dashboard/edit_user.html',context)

def delete_user(request,pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('users')
