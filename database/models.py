from django.db import models

# Create your models here.
class Student(models.Model):
    s_profile = models.ImageField(upload_to='pics')
    s_name=models.CharField(max_length=50)
    s_pass=models.CharField(max_length=20)
    s_branch=models.CharField(max_length=5)
    s_year=models.IntegerField()

class Teacher(models.Model):
    t_profile = models.ImageField(upload_to='pics')
    t_name=models.CharField(max_length=50)
    t_pass=models.CharField(max_length=20)

class TeacherUpload(models.Model):
    send_name=models.CharField(max_length=50)
    branch=models.CharField(max_length=5)
    year=models.IntegerField()
    sub_id=models.CharField(max_length=10)
    upload_file=models.FileField(upload_to='downloads')

class StudentUpload(models.Model):
    send_name=models.CharField(max_length=50)
    t_name=models.CharField(max_length=50)
    branch=models.CharField(max_length=5)
    year=models.IntegerField()
    sub_id=models.CharField(max_length=10)
    upload_file=models.FileField(upload_to='downloads')

class Branches(models.Model):
    id=models.CharField(primary_key=True,max_length=10)
    teacher_name=models.CharField(max_length=50)
    branch=models.CharField(max_length=5)
    year=models.IntegerField()