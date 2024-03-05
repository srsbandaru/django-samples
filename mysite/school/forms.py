from django.forms import ModelForm
from school.models import School

class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = "__all__"