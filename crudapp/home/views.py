from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student

def dashboard(request):
    students = Student.objects.all()
    return render(request, 'dashboard.html', {'students': students})


def dataAdd(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        class_name = request.POST.get('class')
        address = request.POST.get('address')
        
        student = Student(name=name, class_name=class_name, address=address)
        student.save()
        
        return redirect('dash')
    
    return render(request, 'adddata.html')
    
def deleteData(request,student_id):
    student = Student.objects.get(pk=student_id)
    
    if request.method == 'POST':
        student.delete()
        return redirect('dash')
    
    return render(request, 'deletedata.html', {'student': student})
    
def editData(request, student_id):
    student = Student.objects.get(pk=student_id)
    
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.class_name = request.POST.get('class')
        student.address = request.POST.get('address')
        student.save()
        return redirect('dash')
    
    return render(request, 'edit.html', {'student': student})