from django.urls import path
from .views import new_job, available_jobs, new_message

urlpatterns = [
    path('new_job/', new_job, name='new_job'),
    path('available/', available_jobs, name='available_jobs'),
    path('new_message/', new_message, name='new_message'),
]
