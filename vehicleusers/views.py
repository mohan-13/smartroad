from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import views as authviews
from onroad.models import checkdetails
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'vehicleusers/home.html')

def signup(request):
    form = SignUpForm(request.POST)

    if form.is_valid():
        password = form.cleaned_data.get("password")
        confirm_password = form.cleaned_data.get("confirm_password")
        if password==confirm_password:
            form.save()
            return redirect('login')
        else:
            form.add_error('confirm_password', 'The passwords do not match')

    else:
        form = SignUpForm()
    return render(request, 'vehicleusers/signup.html', {'form': form})

def mylogin(request):
    if request.user.is_authenticated:
        return redirect("update")
    else:
        return authviews.login(request)
def profile(request):

    if request.user.is_authenticated:
        er=1
        ai=request.user.id
        data1 = user.objects.get(base_user_id=ai)
        atype=data1.user_type
        x = userdetails.objects.get(userid=data1.base_user)
        y = vehicledetails.objects.filter(userid=data1.base_user)
        adhar=data1.aadhar_id
        lic = x.licensenum
        # veh=y.regno
        fine=data1.fine
        finedet=checkdetails.objects.filter(driver=data1.aadhar_id)
        args={'adhar':adhar,'lic':lic,'veh':y,'fine':fine,'finedet':finedet,"er":er,"acc":atype}
    else:
        er=0
        args={'er':er}
    return render(request,'vehicleusers/myprofile.html',args)



def updateprofile(request):
    form=detailsform(request.user)
    if request.method=="POST":
        form = detailsform(request.user, request.POST)
        if form.is_valid():
            det=form.save()
        else:
            form=detailsform(request)
    return render(request,'vehicleusers/updateprofile.html',{'form':form})

def addvehicle(request):
    form=vehicleform(request.user)
    if request.method=="POST":
        form = vehicleform(request.user, request.POST)
        if form.is_valid():
            form.save()
        else:
            form=vehicleform(request)
    return render(request,'vehicleusers/updatevehicle.html',{'form':form})

# Create your views here.
