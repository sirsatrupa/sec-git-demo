from django.db import models

# Create your models here.
class Batch(models.Model):
    batch_no = models.CharField(max_length=30,unique=True)
    module_name = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    lab_no = models.IntegerField()

    def __str__(self):
        return self.module_name

# model for Feedback
class Feedback(models.Model):
    username=models.CharField(max_length=30)
    created_date=models.DateTimeField(auto_now_add=True)
    feedback=models.TextField()

    def __init__(self):
        return self.username

course_ch = [
    ("Web Designing", "Web Designing"),
    ("Full Stack Python", "Full Stack Python"),
    ("Data Science", "Data Science"),
    ("Web Development","Web Development"),
]

# model for Contact
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    contact=models.IntegerField()
    course=models.CharField(max_length=30,choices=course_ch)
    help=models.TextField()

    def __init__(self):
        return self.name