from django.shortcuts import render
from django.views import View

# Create your views here.
class SchoolListView(View):
    template = 'school/school_list.html'

    def get(self, request):
        return render(request, self.template)