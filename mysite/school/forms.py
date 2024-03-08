from django.forms import ModelForm
from school.models import School, Student

# School Form
class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = "__all__"

# Student Form
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"