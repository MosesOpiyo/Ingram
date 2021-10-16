from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('users/',include('users.urls')),
    path('',views.welcome,name = 'welcome'),

]