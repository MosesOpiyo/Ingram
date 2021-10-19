from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from gram.forms import PictureForm, ProfileForm
from gram.models import Picture, Profile

def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    post = Picture.objects.filter(user=request.user)
    profile = Profile.objects.get(user=request.user)
   

    return render(request,'all-grams/home.html',{'post':post,'profile':profile})

def explore(request):
    return render(request,'all-grams/explore.html')

def profile(request):
    profile = Profile.objects.get(user=request.user)
    
    return render(request,'all-grams/profile.html',{'profile':profile})

def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
          

            return redirect('profile')
        else:
            return redirect('update_profile')

    else: 
       form = ProfileForm(instance=request.user.profile)
       return render (request,'all-grams/update_profile.html',{"form":form})

def make_a_post(request):
    
    post = Picture(user=request.user)

    if request.method == 'POST':
        
         form = PictureForm(request.POST,request.FILES,instance=post)
         if form.is_valid():
            form.save()
            
            return redirect('home')
         else:
           
            return redirect('Make_a_post')


    else:
        form = PictureForm(instance=post)
        return render(request,'all-grams/post.html',{"form":form})
        

    

