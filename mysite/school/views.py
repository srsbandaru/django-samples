from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from school.models import School
from school.forms import SchoolForm
from django.contrib.auth.mixins import LoginRequiredMixin

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
    
# School Create View
class SchoolCreate(LoginRequiredMixin, View):
    template = "school/school_form.html"
    success_url = "school:all"

    def get(self, request):
        form = SchoolForm()
        context = {
            'form':form
        }
        return render(request, self.template, context)
    
    def post(self, request):
        form = SchoolForm(request.POST)
        if not form.is_valid():
            context = {
                'form':form
            }
            return render(request, self.template, context)
        form.save()
        return redirect(self.success_url)

# School Details View
class SchoolDetail(View):
    model = School
    template = 'school/school_detail.html'

    def get(self, request, pk):
        school = get_object_or_404(self.model, id=pk)
        context = {
            'school':school
        }
        return render(request, self.template, context)
    
# School Update View
class SchoolUpdate(LoginRequiredMixin, View):
    model = School
    template = 'school/school_form.html'
    success_url = "school:all"

    def get(self, request, pk):
        school = get_object_or_404(self.model, id=pk)
        form = SchoolForm(instance=school)
        context = {
            'form':form
        }
        return render(request, self.template, context)
    
    def post(self, request, pk):
        school = get_object_or_404(self.model, id=pk)
        form = SchoolForm(request.POST,instance=school)
        if not form.is_valid():
            context = {
                'form':form
            }
            return render(request, self.template, context)
        form.save()
        return redirect(self.success_url)

# School Delete View
class SchoolDelete(LoginRequiredMixin, View):
    model = School
    template = 'school/school_confirm_delete.html'
    success_url = "school:all"

    def get(self, request, pk):
        school = get_object_or_404(self.model, id=pk)
        context = {
            'school':school
        }
        return render(request, self.template, context)
    
    def post(self, request, pk):
        school = get_object_or_404(self.model, id=pk)
        school.delete()
        return redirect(self.success_url)
    
  