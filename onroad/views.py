from django.shortcuts import render,HttpResponse,render_to_response,redirect
from .forms import *
from vehicleusers.models import *
from django.utils import timezone
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def checking(request):
    if request.user.is_authenticated():
        id = request.user.id
        cuser = user.objects.get(base_user_id=id)

        if (cuser.user_type == 1):
            form = checkingform(request.POST)
            id = request.user.id
            cuser = user.objects.get(base_user_id=id)

            if form.is_valid():
                data = form.cleaned_data
                licnum = data['licnum']
                aadharnum = data['aadhar']
                vehnum = data['vehnum']

                try:
                    y = vehicledetails.objects.get(regno=vehnum)
                    veh = y.regno
                except vehicledetails.DoesNotExist:
                    veh = 0

                # hel=x.helmetid
                try:
                    data1 = user.objects.get(aadhar_id=aadharnum)
                    x = userdetails.objects.get(userid=data1.base_user)
                    lic = x.licensenum
                    if lic == licnum:
                        ls = "LICENSE VERIFIED"
                        lic_fine = 0
                    else:
                        ls = "LICENSE NOT FOUND"
                        lic_fine = 100
                    if veh == vehnum:
                        vs = "VEHICLE NUMBER VERIFIED"
                        veh_fine = 0
                    else:
                        vs = "VEHICLE NUMBER NOT FOUND"
                        veh_fine = 100
                    x = lic_fine + veh_fine
                    data1.fine = data1.fine + x
                    data1.fine_date = timezone.now()
                    data1.save()
                    reason=ls+" , "+vs
                    form.save(x, request,reason)
                    sender=data1.base_user
                    print(sender)
                    # msg= "HI!!!!"+str(aadharnum)+".Your Checking Status:"+ls+" with ID "+str(licnum)+"."+vs+" with Reg.NO: "+str(vehnum)+" . Your Total Fine: "+str(x)+"  Thank You"
                    # g = send_mail('Smart Road Checking Portal ', msg, settings.EMAIL_HOST_USER,
                    #               [sender], fail_silently=False)

                    args = {'license': ls, 'vehicle': vs,'fine':x}

                    return render(request, 'onroad/postchecking.html', args)
                except user.DoesNotExist:
                    return HttpResponse(
                        "<title>Contact MODI JI</title><h1>Your Aadhar Missing <p>Contact Modi jiiiiiiiiiiiiiiiiii!!!!!!!!!!!!!!!!!!!!!!!!!@</p><p>modiji@gmail.com </p>")


            else:
                form = checkingform()
                messages.info(request,"Please provide correct Credentials",)
                return render(request, 'onroad/checking.html', {'form': form})
        else:
            return HttpResponse("<h1>You are not authenticated to access this page</h1><a  href= logout>LOG0UT</a> ")
    else:
        return redirect('login')




