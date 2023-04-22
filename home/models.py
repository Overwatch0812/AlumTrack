from django.db import models

# Create your models here.
class Event(models.Model):
    img=models.ImageField(upload_to='pics')
    event_name=models.CharField(max_length=200)
    committee_name=models.CharField(max_length=200)
    Entry_fee=models.IntegerField()
    location=models.CharField(max_length=200)
    date_time=models.DateTimeField()
    description=models.TextField()

class Blog(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField()
    date=models.DateField()

class New(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField()
    date=models.DateField()

class Contact(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    mail=models.EmailField()
    subject=models.CharField(max_length=100,null=True,blank=True)
    message=models.TextField()