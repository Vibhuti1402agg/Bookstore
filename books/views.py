from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import info,data
from .forms import registrationform,addbook

def home(request):
    books=info.objects.all()
    return render(request,'homepage.html',{'books':books})

def register(request):
    form=registrationform
    return render(request,'form.html',{'form':form})

def adduser(request):
    form= registrationform(request.POST)

    if form.is_valid():
        register= data(username=form.cleaned_data['username'],email= form.cleaned_data['email'], password= form.cleaned_data['password'])

        register.save()

    return redirect(home)

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



