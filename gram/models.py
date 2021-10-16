from django.db import models
from django.db.models.fields import TextField
from django.db.models.fields.files import ImageField

class Comments(models.Model):
    description = TextField(blank=True)

    def save_comment(self):
        """
        This adds a category to the database
        """
        self.save()

    def delete_comment(self):
        """
        This removes a category from the database
        """
        self.delete()

    def update_comment(self,new):
        """This will update a category
        Args:
            new ([type]): [description]
        """
        self.name = new.description
        self.save()

    def __str__(self):
        return self.name




class User(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    username = models.CharField(max_length =50)
    email = models.EmailField()
    

class Picture(models.Model):
    image = ImageField('image')
    description = models.TextField(blank=True)
    post_date = models.DateField(auto_now_add=True)
    likes = models.IntegerField()
    comments = models.ForeignKey(Comments,on_delete=models.CASCADE)



