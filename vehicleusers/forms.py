from django import forms
from .models import *
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    email=forms.EmailField()
    class Meta:
        model = user
        fields = ('aadhar_id','email','password', 'confirm_password',)

    def save(self, commit=True):
        data = self.cleaned_data
        password = data['password']
        aadhar_id = data['aadhar_id']
        email=data['email']
        user_obj = User.objects.create_user(username=email,email=email, password=password)
        user.objects.create( aadhar_id=aadhar_id,base_user=user_obj)
        return user_obj
class detailsform(forms.ModelForm):
    def __init__(self, user,*args, **kwargs):
        super(detailsform, self).__init__(*args, **kwargs)
        self.user = user
    class Meta:
        model = userdetails
        fields = ['licensenum','helmetid']

    def save(self, commit=True):
        data = self.cleaned_data
        licensenum=data['licensenum']
        helmetid=data['helmetid']
        det_obj=userdetails.objects.create(licensenum=licensenum,helmetid=helmetid,userid=self.user)
        return det_obj


class vehicleform(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(vehicleform, self).__init__(*args, **kwargs)
        self.user = user

    class Meta:
        model = vehicledetails
        fields = ['regno', 'insuranceid']

    def save(self, commit=True):
        data = self.cleaned_data
        regno = data['regno']
        insuranceid = data['insuranceid']
        veh_obj = vehicledetails.objects.create(regno=regno,insuranceid=insuranceid, userid=self.user)
        return veh_obj



