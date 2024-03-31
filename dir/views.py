from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    employees = Employee.objects.all()

    return render(request, 'dir/employee.html', {'employees': employees})