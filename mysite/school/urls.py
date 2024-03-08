from django.urls import path
from . import views

app_name = "school"

urlpatterns = [
    path('', views.SchoolList.as_view(), name = "all"),
    path("create", views.SchoolCreate.as_view(), name = "school_create"),
    path('detail/<int:pk>', views.SchoolDetail.as_view(), name = "school_detail"),
    path('update/<int:pk>', views.SchoolUpdate.as_view(), name = "school_update"),
    path('delete/<int:pk>', views.SchoolDelete.as_view(), name = "school_delete"),
    path('student', views.StudentList.as_view(), name = "student_list"),
    path('student/create', views.StudentCreate.as_view(), name = "student_create")
]