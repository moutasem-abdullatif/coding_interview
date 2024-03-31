from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):

    q = request.GET.get('q','')
    employees = Employee.objects.filter(first_name__icontains=q)
    
    if request.headers.get('hx-Request') != None:
        template_name = 'dir/partial.html'
    else:
        template_name = 'dir/employee.html'

    context = {'employees': employees}
    return render(request, template_name, context)