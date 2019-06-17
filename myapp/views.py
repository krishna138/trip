from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import CreateView

from .myforms import Login, Register
from .models import Post
# Create your views here.

def home(request):
    a = Post.objects.all()
    user = False
    try:
        myid = int(request.session.get('user'))
        user = User.objects.get(id=myid)
        if user.is_authenticated:
            pass
        else:
            user = False

    except:
        pass
    return render(request, 'myapp/home.html', {'val': a,'user':user})

def detailPost(request,id):
   # a=Album.objects.get(id=id)
   a=Post.objects.filter(city__contains=id)
   user = False
   try:
       myid = int(request.session.get('user'))
       user = User.objects.get(id=myid)
       if user.is_authenticated:
           pass
       else:
           user = False
   except:
       pass
   return render(request,'myapp/detailPost.html',{'val':a,'user':user})

def book(request):

    return render(request, 'myapp/book.html')

def loginpage(request):
    print('hello')
    form=Login(request.POST or None)
    if form.is_valid():
        val=request.GET.get('next')
        u=form.cleaned_data.get('Username')
        p=form.cleaned_data.get('Password')
        val2=authenticate(username=u,password=p)
        request.session['user'] = val2.id
        print(val2)
        login(request,val2)
        if val:
            return redirect(val)
        else:
            return redirect('myapp:home')
    return render(request,'myapp/login.html',{'form':form,'user':False})

def signout(request):
    try:
        del(request.session['user'])
    except:
        pass
    logout(request)
    return redirect('myapp:home')

def signuppage(request):
    form= Register(request.POST or None)
    if form.is_valid():
        data=form.save(commit=False)
        p=form.cleaned_data.get('password')
        data.set_password(p)
        data.save()
        return redirect('/login')
    return render(request,'myapp/login.html',{'form':form,'user':False})

class Addplace(LoginRequiredMixin,CreateView):
    template_name = 'myapp/login.html'
    model = Post
    login_url='myapp:login'
    fields=['loc','city','desc','price','img','show']
    context_object_name = 'form'