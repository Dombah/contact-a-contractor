"""
URL configuration for contactacontractor project.

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
from django.urls import path, include
from app.views import home, register, user_dashboard, user_profile, new_job, contractor_dashboard, contractor_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register, name='register'),
    path('account/user_dashboard/', user_dashboard, name='user_dashboard'),
    path('account/user_profile/', user_profile, name='user_profile'),
    path('jobs/new', new_job, name='new_job'),
    path('account/contractor_dashboard/', contractor_dashboard, name='contractor_dashboard'),
    path('account/contractor_profile/', contractor_profile, name='contractor_profile'),
]
