from django.shortcuts import render
from .models import Department
from django.views import View

# Create your views here.

# Department List View
class DepartmentList(View):
    template = 'employee/department_list.html'

    def get(self, request):
        department_list = Department.objects.all()
        context = {
            'department_list':department_list
        }
        return render(request, self.template, context)
    

    
