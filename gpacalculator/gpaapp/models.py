# gpaapp/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    # Add other student information fields

class Course(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    grade = models.FloatField()