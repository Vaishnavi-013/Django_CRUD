from django.http import HttpResponse
import datetime
from django.shortcuts import render

def home(request):
    date= datetime.datetime.now()
    print("test function is called from view")
   # return HttpResponse("<h1>Hello<h1>"+str(date))
    return render(request,"home.html",{})

def about(request):
   # return HttpResponse("<h1> This is about page</h1>")
   return render(request,"about.html",{})
def services(request):
    return HttpResponse("<h1> This is services page</h1>")