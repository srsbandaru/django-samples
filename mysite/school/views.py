from django.shortcuts import render, get_object_or_404
from django.views import View
from school.models import School

# Create your views here.

# School list view
class SchoolList(View):
    template = 'school/school_list.html'

    def get(self, request):
        school_list = School.objects.all()
        context = {
            'school_list':school_list
        }
        return render(request, self.template, context)
    
class SchoolDetail(View):
    model = School
    template = 'school/school_detail.html'

    def get(self, request, pk):
        school = get_object_or_404(self.model, id=pk)
        context = {
            'school':school
        }
        return render(request, self.template, context)
  