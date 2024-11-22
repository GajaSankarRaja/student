from django.shortcuts import render,redirect
from .models import Student

def student_list(request):
    if request.method=='POST':
        name=request.POST['name']
        roll_number=request.POST['roll_number']
        email=request.POST['email']
        Student.objects.create(name=name,roll_number=roll_number,email=email)
        return redirect('student_list')
    students=Student.objects.all()
    return render(request,'student_list.html',{'students':students})

# Create your views here.
