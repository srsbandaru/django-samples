from django.shortcuts import render, redirect, get_object_or_404
from .models import Department
from employee.forms import DepartmentForm
from django.views import View
from django.contrib import messages

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
    
# Create Department View
class CreateDepartment(View):
    template = 'employee/department_form.html'
    success_url = 'employee:all'

    def get(self, request):
        form = DepartmentForm()
        context = {
            'form':form
        }
        return render(request, self.template, context)
    
    def post(self, request):
        form = DepartmentForm(request.POST)
        if not form.is_valid():
            context = {
                'form':form
            }
            return render(request, self.template, context)
        form.save()
        messages.success(request, "Department was successfully created.")
        return redirect(self.success_url)
    
# Edit Department View 
class EditDepartment(View):
    model = Department
    template = "employee/department_form.html"
    success_url = "employee:all"
    
    def get(self, request, pk):
        department = get_object_or_404(self.model, id=pk)
        form = DepartmentForm(instance=department)
        context = {
            'form':form
        }
        return render(request, self.template, context)
    
    def post(self, request, pk):
        department = get_object_or_404(self.model, id=pk)
        form = DepartmentForm(request.POST,instance=department)
        if not form.is_valid():
            context = {
                'form':form
            }
            messages.error(request, "Please enter all the required details.")
            return render(request, self.template, context)
        form.save()
        messages.success(request, "Department was successfully updated.")
        return redirect(self.success_url)
    
# Delete Department View
class DeleteDepartment(View):
    model = Department
    template = "employee/department_confirm_delete.html"
    success_url = "employee:all"

    def get(self, request, pk):
        department = get_object_or_404(self.model, id=pk)
        context = {
            "department":department
        }
        return render(request, self.template, context)
    
    def post(self, request, pk):
        department = get_object_or_404(self.model, id=pk)
        department.delete()
        messages.info(request, "Department was successfully deleted.")
        return redirect(self.success_url)