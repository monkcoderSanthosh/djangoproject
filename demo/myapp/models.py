from django.db import models

class Stud_record(models.Model):
    username=models.CharField( max_length=200)
    password=models.CharField( max_length=200)
    gmail=models.CharField( max_length=200)
    phone=models.CharField( max_length=10)
    user_username=models.CharField( max_length=100)
