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

from django.urls import path
from accounts.views import register, user_dashboard, user_profile, contractor_dashboard, contractor_profile

app_name = "accounts"
urlpatterns = [
    path('register/', register, name='register'),
    path('user_dashboard/', user_dashboard, name='user_dashboard'),
    path('user_profile/', user_profile, name='user_profile'),
    path('contractor_dashboard/', contractor_dashboard, name='contractor_dashboard'),
    path('contractor_profile/', contractor_profile, name='contractor_profile'),
]