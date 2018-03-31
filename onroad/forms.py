from django import forms
from vehicleusers.models import *
from .models import checkdetails
from django.contrib.auth.models import User


class checkingform(forms.ModelForm):
    aadhar=forms.CharField(max_length=12)
    licnum=forms.CharField(max_length=100)
    vehnum=forms.CharField(max_length=10)
    class Meta:
        model = checkdetails
        fields = ('aadhar','licnum','vehnum' )


    def save(self, y,request,rea,commit=True):
        data=self.cleaned_data
        daadhar=data["aadhar"]
        x = User.objects.get(id=request.user.id)
        cuser = user.objects.get(base_user_id=x)
        caadhar=cuser.aadhar_id
        check_obj=checkdetails.objects.create(checked_by=caadhar,driver=daadhar,fine_imp=y,checked_on=timezone.datetime.now(),fine_reason=rea)
        return check_obj




