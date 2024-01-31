from django.urls import path
from .views import new_job

urlpatterns = [
    path('new/', new_job)
]
