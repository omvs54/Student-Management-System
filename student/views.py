from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# 🏠 Dashboard - View & Add Students
def dashboard(request):
    students = Student.objects.all().order_by('roll_no')
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    return render(request, 'student/dashboard.html', {
        'students': students,
        'form': form
    })

# 🗑️ Delete Student
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('dashboard')
