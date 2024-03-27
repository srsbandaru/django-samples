from django.forms import ModelForm
from employee.models import Department

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = "__all__"
        