from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100) #columns
    tagline = models.TextField() #columns

    # def __str__(self):
    #     return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class userregister(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    add = models.TextField()
    password = models.CharField(max_length=20)

    # def __str__(self):
    #     return self.name

class img(models.Model):
    img= models.ImageField(upload_to='VKimg')

class category(models.Model):
    name= models.CharField(max_length=50)
    image=models.ImageField(upload_to='vkimg')

    def __str__(self):
        return self.name
