# gpaapp/views.py
from django.shortcuts import render, redirect
from .forms import CourseForm

def calculate_gpa(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            # Calculate GPA logic goes here
            return redirect('result_page')  # Redirect to a page displaying GPA
    else:
        form = CourseForm()

    return render(request, 'gpaapp/calculate_gpa.html', {'form': form})
