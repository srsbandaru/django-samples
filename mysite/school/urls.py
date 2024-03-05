from django.urls import path
from . import views

app_name = "school"

urlpatterns = [
    path('', views.SchoolList.as_view(), name = "all"),
    path('detail/<int:pk>', views.SchoolDetail.as_view(), name = "school_detail"),
    path('update/<int:pk>', views.SchoolUpdate.as_view(), name = "school_update")
]