from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as authviews

urlpatterns=[

    url(r'^checking/',views.checking),

    ]