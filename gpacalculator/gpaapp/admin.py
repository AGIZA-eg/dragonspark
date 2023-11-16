# gpaapp/admin.py
from django.contrib import admin
from .models import Student, Course

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', )  # Add other fields you want to display in the list

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('student', 'course_name', 'grade')  # Add other fields you want to display in the list
    list_filter = ('student', )  # Add filters if needed
    search_fields = ('student__name', 'course_name')  # Add fields for search if needed
