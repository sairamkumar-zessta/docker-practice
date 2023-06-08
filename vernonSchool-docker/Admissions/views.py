from django.shortcuts import render
from .models import Student 
from .forms import StudentModelForm
# Create your views here.
def home(request):
    return render(request, 'index.html')
def add_admission(request):
    req = {'forms' : StudentModelForm}
    
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request,'admissions/add_admission.html',req) 
    
def admission_report(request):
    result = Student.objects.all()
    students = {'allstudents':result}
    return render(request,'admissions/admission_rep.html',students) 