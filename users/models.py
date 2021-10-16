from django.db import models
from gram.models import Comments, Picture

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=70)
    confirm_password = models.CharField(max_length=70)
    picture = models.ForeignKey(Picture,on_delete=models.CASCADE)
    comments = models.ForeignKey(Comments,on_delete=models.CASCADE)


