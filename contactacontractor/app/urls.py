from django.urls import path
from .views import new_job, available_jobs

urlpatterns = [
    path('new/', new_job, name='new_job'),
    path('available/', available_jobs, name='available_jobs'),
]
