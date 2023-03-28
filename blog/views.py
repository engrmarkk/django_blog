from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from .models import User, BlogPost
import random


# Create your views here.
def index(request):
    datas = BlogPost.objects.all()
    if datas:
        datas = list(datas)
    random.shuffle(datas)
    return render(request, "index.html", {"datas": datas})


@login_required
def welcomepage(request):
    blogs = BlogPost.objects.filter(user=request.user)
    if request.method == "POST":
        title = request.POST.get('title')
        image = request.FILES.get('image')
        content = request.POST.get('content')
        if not all([title, content]):
            messages.error(request, "Title and Post content required")
            return redirect('/welcome')

        user = User.objects.get(username=request.user.username)
        blog = BlogPost.objects.create(post_title=title,
                                       post_content=content,
                                       img=image, user=user)
        blog.save()
        messages.info(request, 'Blog created')
        return redirect('/welcome')
    return render(request, "welcomepage.html", {'blogs': blogs})


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        check_if_user_exist = User.objects.filter(username=username.lower()).exists()
        if check_if_user_exist:
            user = authenticate(request, username=username.lower(), password=password)
            if user is not None:
                auth.login(request, user)
                messages.info(request, "Logged in successfully")
                return redirect("/")
            else:
                messages.info(request, "wrong credentials")
                return redirect("/login")
    return render(request, "login.html")


def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password")
        password2 = request.POST.get("confirmpassword")
        if not all([first_name, last_name, username, email, password1]):
            messages.error(request, "All fields are required")
            return redirect("/register")
        if password1 == password2:
            if User.objects.filter(username=username.lower()).exists():
                messages.error(request, "Username is taken")
                return redirect("/register")
            elif User.objects.filter(email=email.lower()).exists():
                messages.error(request, "Email is taken")
                return redirect("/register")
            else:
                user = User.objects.create_user(
                    username=username.lower(),
                    email=email.lower(),
                    password=password1,
                    first_name=first_name.lower(),
                    last_name=last_name.lower(),
                )
                user.save()
                messages.success(request, "User created successfully.")
                return redirect("/login")
        messages.error(request, "Password unmatched")
        return redirect("/register")
    return render(request, "register.html")


@login_required
def logout(request):
    auth.logout(request)
    return redirect("/")


@login_required
def delete_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    post.delete()
    messages.success(request, "Post deleted successfully")
    return redirect("/welcome")


@login_required
def update_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")
        if title:
            post.post_title = title
        if content:
            post.post_content = content
        if image:
            post.img = image
        post.save()
        messages.success(request, "Post updated successfully")
        return redirect("/welcome")
    return render(request, "update.html", {'post': post})


def display_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    return render(request, 'display.html', {'post': post})
