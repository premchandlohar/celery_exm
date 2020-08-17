from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Userprofile(models.Model):

    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=255,unique=False)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    

