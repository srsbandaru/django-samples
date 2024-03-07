"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.views.generic.base import TemplateView
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROUTE = os.path.join(BASE_DIR, "site")

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^site/(?P<path>.*)$',serve,
            {'document_route':SITE_ROUTE, "show_indexes":True}, name="site_path"
            ),
    path("", TemplateView.as_view(template_name='home/main.html')),
    path("school/", include("school.urls")),
    path("accounts/", include("django.contrib.auth.urls"))
]
