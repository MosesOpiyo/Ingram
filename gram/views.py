from django.shortcuts import render

def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    return render(request,'all-grams/home.html')

def explore(request):
    return render(request,'all-grams/explore.html')

def profile(request):
    return render(request,'all-grams/profile.html')