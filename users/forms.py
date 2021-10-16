from django.forms import ModelForm, fields
from users.models import User

class UserForm(ModelForm):
    class meta:
        model = User
        fields = ['fisrt_name','last_name','username','email','password','confirm_password']