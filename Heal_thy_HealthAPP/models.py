from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from embed_video.fields import EmbedVideoField
from datetime import date,datetime


class Category(models.Model):
    tag = models.CharField(max_length = 100)
    
    def __str__(self):
        return str(self.tag)
    
    class Meta :
        db_table = "Category"

class Video(models.Model):
    title = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    added = models.DateTimeField(auto_now_add = True)
    url = EmbedVideoField(null = True, blank = True)
    def __str__(self):
        return str(self.title)
    class Meta:
        ordering = ['-added']
        db_table = "Video"
    
    
class Person(models.Model):
    user = models.OneToOneField(User,null = True,on_delete=models.CASCADE)
    Gender = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others")
    )
    
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10,choices=Gender)
    
    height = models.PositiveSmallIntegerField() #in cm
    weight = models.PositiveSmallIntegerField() #in Kg
    
    preferences  = models.ManyToManyField(to=Category,null=True,blank = True)
    @property
    def Age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        
    @property
    def BMI(self):
        self.height = self.height/100 # in m
        bmi = self.weight/(self.height*self.height)
        
        if bmi < 18.5:
            status =  "Underweight"
        elif bmi < 25:
            status =  "Normal"
        elif bmi < 30:
            status =  "Overweight"
        else:
            status =  "Obese"
        return (bmi, status)
    
    
    def __str__(self):
        return str(self.name)
    class Meta:
        db_table = "Person"
    
    
    
    
    
    
    
    
    
    
	