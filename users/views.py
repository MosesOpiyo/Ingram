from django.shortcuts import render
from users.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password,confirm_password=confirm_password )

   
    return render(request,'auth/register.html')

def login_user(request):
    return render(request,'auth/login.html')