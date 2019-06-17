from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

# Create your models here.

#Blog model
from django.urls import reverse
from star_ratings.models import Rating


class Post(models.Model):
    loc=models.CharField(max_length=50,help_text="Enter Place name")
    city = models.CharField(max_length=50, help_text="Enter city name")
    desc=models.CharField(max_length=500,help_text="Enter Description")
    price=models.IntegerField(help_text="Enter Booking Price")
    img = models.CharField(max_length=100, help_text='add url of image')
    show=models.BooleanField(help_text="Enter 0 if post is private")

    def __str__(self):
        # passing value at time of post objcet calling
        return '{}{}'.format(self.loc, self.price)

    def get_absolute_url(self):
        return reverse('myapp:home')

class Rate(models.Model):
    ratings=GenericRelation(Rating, related_query_name='foos')
    s_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    u_id=models.ForeignKey(User,on_delete=models.CASCADE)




