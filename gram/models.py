from django.db import models
from django.db.models.fields import CharField, TextField
from django.db.models.fields.files import ImageField

class User(models.Model):
    username = CharField(max_length=50)
    bio = TextField(blank=True)

class Comments(models.Model):
    comment = TextField(blank=True)

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
    

class Picture(models.Model):
    image = ImageField(upload_to='image/',blank=True)
    description = models.TextField(blank=True)
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name="likers",blank=True)
    comments = models.ForeignKey(Comments,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_picutre(self):
        self.save()


    def get_picture_by_id(id):
        picture = Picture.objects.get(pk=id)
        return picture

    def save_picture(self):
         self.save()

    def delete_picture(self):
        """This deletes the image from the database using its pk
        Args:
            id ([type]): [description]
        """
        self.delete()
    
    def update_picture(self,new):
        """This method will update a record of an image
        """
        
        self.image = new.image
        self.description = new.description
        self.post_date = new.post_date
        self.likes = new.likes
        self.save()

    @classmethod
    def get_images(cls,users):
        posts = []
        for user in users:
            pictures = Picture.objects.filter(user = user)
            for picture in pictures:
                posts.append(picture)

        return posts
