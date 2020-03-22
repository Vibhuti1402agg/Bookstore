from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import info,data
from .forms import registrationform,addbook,loginform
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate,get_user_model,login,logout

def home(request):
    books=info.objects.all()
    return render(request,'homepage.html',{'books':books})


def adduser(request):
    next= request.GET.get('next')
    form=registrationform(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        password=form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user=authenticate(username=user.username,password=password)
        login(request,new_user)
        if next:
            return redirect(next)
        return redirect(home)
    return render(request,'form.html',{'form':form})

def loginuser(request):
    next = request.GET.get('next')
    form = loginform(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect(home)
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect(home)


@staff_member_required
def newbook(request):
    if request.method == "POST":
        form1 = addbook(request.POST)
        if form1.is_valid():
            post = form1.save(commit=False)
            post.save()
            return redirect(home)
    else:
        form1= addbook()
        return render(request, 'new.html', {'form1': form1})

def cart(request):
    return HttpResponse('welcome to the cart')

@staff_member_required
def editbook(request,book_id):
    book=info.objects.get(id=book_id)
    if request.method == "POST":
        form1=addbook(request.POST,instance=book)
        if form1.is_valid():
            form1.save()
            return redirect(home)
    else:
        form1= addbook()
        return render(request, 'new.html', {'form1': form1})





