from django.shortcuts import render
from gram.forms import PictureForm
from gram.models import Picture

def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    return render(request,'all-grams/home.html')

def explore(request):
    return render(request,'all-grams/explore.html')

def profile(request):
    return render(request,'all-grams/profile.html')

def picture(request):
    if request.method == 'POST':
        form = PictureForm(request.POST)
        form.save()
        picture = Picture.objects.all()

        return render(request,'home.html',{'picture':picture})

