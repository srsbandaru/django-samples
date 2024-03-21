from django.shortcuts import render
from django.views import View

# Create your views here.

# Department List View
class DepartmentList(View):
    template = 'employee/department_list.html'

    def get(self, request):
        return render(request, self.template)
