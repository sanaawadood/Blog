from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from .forms import SignUpForm
from lxml.html import html5parser

from .models import Post, Comment
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'blogg/index.html')

def signup(request):

    if request.method == 'POST':
        signform = SignUpForm(data = request.POST)

        print ("form.is_valid()-> ", signform.is_valid(), " " , signform.errors)

        if signform.is_valid():
            user = signform.save(commit = False)
            usr = signform.cleaned_data['username']
            user.username = usr
            #print(user.username)
            password = signform.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=usr, password=password)
            login(request, user)

            return render(request, 'blogg/index.html')

        else:
            return render(request, 'blogg/signup.html', {
                'form':signform,
                'error_message':"Invalid entries" ,
            })
    else:
        signform = SignUpForm()

    return render(request, 'blogg/signup.html',{'form':signform})


def logout_user(request):

    logout(request)
    return render(request, 'blogg/index.html')


def login_user(request):

    usr = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=usr, password=password)

    if user is not None:
        login(request, user)
    else:
        return render(request, 'blogg/index.html',{'error_message':"Invalid Input"})

    return render(request, 'blogg/index.html')


def add_post(request):

    if request.method == "POST":

        content = request.POST['content']
        heading = request.POST['heading']
        newpost = Post()
        newpost.writer = request.user
        newpost.heading = heading
        newpost.pub_date = timezone.now()

        #here we Use html5lib to convert an HTML fragment to plain text
        doc = html5parser.fromstring(content)
        newpost.content = doc.xpath("string()")

        newpost.save()

    else:
        return render(request, 'blogg/add_post.html')
    return render(request, 'blogg/index.html')

def view_posts(request):
    all_posts = Post.objects.order_by('-pub_date')
    context = {'all_posts': all_posts}

    if request.method == 'POST':
        newcomment = Comment()
        newcomment.content = request.POST['content']
        pos = Post.objects.get(id = request.POST['of_post'])
        newcomment.of_post = pos
        newcomment.pub_date = timezone.now()
        newcomment.writer = request.user
        print("")
        newcomment.save()
        return redirect('blogg:view_posts',)

    return render(request, 'blogg/view_posts.html', context)
