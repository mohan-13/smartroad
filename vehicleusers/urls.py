from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    url(r'^$',views.home,name="landing_page"),
    url(r'^signup/$',views.signup),
    url(r'^userlogin/$', auth_views.login,name="login"),
    url(r'^myprofile/$',views.profile,name="myprofile"),
    url(r'^vehdet/$',views.vehicledet,name="vehdet"),
    url(r'^finedet/$',views.finedetails,name="finedet"),
    url(r'^logout/$',auth_views.logout,name="logout"),
    url(r'^update/$',views.updateprofile,name="update"),
    url(r'^addvehicle/$',views.addvehicle),
    url(r'^data/$',views.datafetch),
    ]