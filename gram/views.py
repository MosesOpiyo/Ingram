from django.shortcuts import redirect, render
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

def make_a_post(request):

    if request.method == 'POST':
         form = PictureForm(request.POST)
         if form.is_valid():
            form.save()
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']

           
            return redirect('home')
         else:
           
            return redirect('Make_a_post')


    else:
        form = PictureForm()
        return render(request,'all-grams/post.html',{"form":form})
        

    

