from django.shortcuts import render,redirect
from lawfirmmanagementsystem.models import LawyerDetails,CaseDetail
from lawfirmmanagementsystem.forms import EnquiryForm,AppointmentForm
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required

def casedetails(request):
    form = CaseDetail.objects.all()
    return render(request,"advocate.html",{'form':form})


def lawyers(request):
    form = LawyerDetails.objects.all()
    return render(request,"lawyer.html",{'form':form})

@login_required(login_url = 'login')
def enquiry(request):
    registered = False
    if request.method == "POST":
        form = EnquiryForm(request.POST,request.FILES)
        if form.is_valid():
            enquiry = form.save()
            enquiry.save()
            registered = True
    else:
        form =  EnquiryForm()
    context = {
        'form':form,
        'registered':registered
    }
    return render(request,"enquiry.html",context)

@login_required(login_url = "login")
def appointment(request):
    registered = False
    if request.method == "POST":
        form = AppointmentForm(request.POST,request.FILES)
        if form.is_valid():
            appointment = form.save()
            appointment.save()
            registered = True
    else:
        form = AppointmentForm()
        
    context = {
        'form':form,
        'registered':registered
    }
    return render(request,"appointment.html",context)


