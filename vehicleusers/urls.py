from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as authviews

urlpatterns=[
    url(r'^$',views.home,name="landing_page"),
    url(r'^signup/$',views.signup),
    url(r'^userlogin/$',authviews.login,name="login"),
    url(r'myprofile/$',views.profile,name="myprofile"),
    url(r'^logout/$',authviews.logout,name="logout"),
    url(r'^update/$',views.updateprofile,name="update"),
    url(r'^addvehicle/$',views.addvehicle),
    url(r'^data/$',views.datafetch),
    ]