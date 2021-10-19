from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('users/',include('users.urls')),
    path('',views.welcome,name = 'welcome'),
    path('home/',views.home,name = 'home'),
    path('explore/',views.explore,name='explore'),
    path('profile/',views.profile,name='profile'),
    path('make_a_post/',views.make_a_post,name='make_a_post'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)