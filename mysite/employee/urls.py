from django.urls import path
from . import views

app_name = "employee"

urlpatterns = [
    path('', views.DepartmentList.as_view(), name = 'all'),
    path('department/create/', views.CreateDepartment.as_view(), name = 'create_department'),
    path('department/edit/<int:pk>', views.EditDepartment.as_view(), name = 'edit_department'),
    path('department/delete/<int:pk>', views.DeleteDepartment.as_view(), name = 'delete_department')
]