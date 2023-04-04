from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    username=None
    img=models.ImageField(upload_to='users_img',default='users_img/user.jpg')
    name= models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,unique=True)
    graduation_year=models.IntegerField(null=True,blank=True)
    course_name=models.CharField(max_length=100,null=True,blank=True)
    GR_number=models.CharField(max_length=100,null=True,blank=True)
    is_verified=models.BooleanField(default=False,null=True,blank=True)
    

    objects=CustomUserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]   
