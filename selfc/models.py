from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100)

class Usuarios(models.Model):
    email = models.EmailField(max_length=500,primary_key=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    country = models.CharField(max_length=50)
    discipline = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class Activity(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='activities')
    file_space = models.FileField(upload_to='files/')
    completed_space = models.BooleanField(default=False)


class Admins(models.Model):
    email = models.EmailField(max_length=200,primary_key=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    role = models.CharField(max_length=50,default="admin")

class Tests(models.Model):
    name=models.CharField(max_length=50)
    author = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='tests')
    autocontrol=models.IntegerField()
    liderazgo=models.IntegerField()
    conciencia=models.IntegerField()
    innovacion=models.IntegerField()
    sistemico=models.IntegerField()
    cientifico=models.IntegerField()
