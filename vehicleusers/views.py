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
@login_required(login_url="login")
def user_det(request):
    ai = request.user.id
    data1 = user.objects.get(base_user_id=ai)
    user_list = data1
    return user_list


@login_required(login_url="login")
def profile(request):
    uid = user_det(request)
    if (uid.user_type == 0 or uid.user_type == 1):
        x = userdetails.objects.get(userid=uid.base_user)
        y = vehicledetails.objects.filter(userid=uid.base_user)
        adhar = uid.aadhar_id
        lic = x.licensenum
        fine = uid.fine
        finedet = checkdetails.objects.filter(driver=uid.aadhar_id)
        args = {'adhar': adhar, 'lic': lic, 'veh': y, 'fine': fine, 'finedet': finedet, "acc": uid.user_type,"user":uid.aadhar_id }
        return render(request, 'vehicleusers/myprofile.html', args)
    else:
        form = spform(request.POST)
        if form.is_valid():
            x = 1
            data = form.cleaned_data
            off_addhar = data["road_aadhar"]
            det = checkdetails.objects.filter(checked_by=off_addhar)
            return render(request, 'vehicleusers/spview.html', {'det': det, 'x': x, 'form': form})
        else:
            form = spform()
            return render(request, 'vehicleusers/spview.html', {'form': form})


@login_required(login_url="login")
def vehicledet(request):
    uid = user_det(request)
    c_user=uid.aadhar_id
    vehs = vehicledetails.objects.filter(userid=uid.base_user)
    return render(request,'vehicleusers/vehdet.html',{'veh':vehs,'user':c_user})
@login_required(login_url="login")
def finedetails(request):
    uid = user_det(request)
    finedet = checkdetails.objects.filter(driver=uid.aadhar_id)
    c_user = uid.aadhar_id
    return render(request, 'vehicleusers/finedet.html', {'finedet': finedet, 'user': c_user})




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
def datafetch(request):
    authdaata=User.objects.all()
    data=user.objects.all()
    profdata=userdetails.objects.all()
    vdata=vehicledetails.objects.all()

    return render(request,'vehicleusers/datafetch.html',{'data':data,'authdata':authdaata,'profdata':profdata,'vdata':vdata})
# Create your views here.
