from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Hospital
from django.urls import reverse


# Create your views here.
def hms_home(request):
    
    hmss=Hospital.objects.all()
    return render(request, "hms/home.html",{
        'hmss':hmss
    })

def add_doctor(request):
    
    if request.method=="POST":
        
        #data fetch
        doctor_name=request.POST.get("doctor_name")
        doctor_id=request.POST.get("doctor_id")
        specialization=request.POST.get("specialization")
        contact_information=request.POST.get("contact_information")
        doctor_address=request.POST.get("doctor_address")
        #validate
        
        #create model object and set the data
        h=Hospital()
        h.name=doctor_name
        h.doctor_id=doctor_id
        h.specialization=specialization
        h.contact_information=contact_information
        h.address=doctor_address
        
        #save the object
        h.save()
        #prepare msg
        return redirect("/hms/home")
    return render(request,"hms/add_doctor.html",{})


def delete_hms(request,doctor_id):
    hms=Hospital.objects.get(pk=doctor_id)
    hms.delete()
    return redirect("/hms/home/")

def update_hms(request,doctor_id):
    hms=Hospital.objects.get(pk=doctor_id)
    return render(request,"hms/update_doctor.html",{
        'hms':hms
    })

def do_update_hms(request,doctor_id):
    if request.method=='POST':
        doctor_name=request.POST.get("doctor_name")
        doctor_id_temp=request.POST.get("doctor_id")
        specialization=request.POST.get("specialization")
        contact_information=request.POST.get("contact_information")
        doctor_address=request.POST.get("doctor_address")
        
        h=Hospital.objects.get(pk=doctor_id)
        
        h.name=doctor_name
        h.doctor_id=doctor_id_temp
        h.specialization=specialization
        h.contact_information=contact_information
        h.address=doctor_address
        
        h.save()
        
    return redirect("/hms/home/")
    
