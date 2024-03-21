from django.urls import path
from . import views

app_name = "employee"

urlpatterns = [
    path('', views.DepartmentList.as_view(), name = 'all')
]