from django.urls import path
from .views import new_job, available_jobs, new_message, new_quote

urlpatterns = [
    path('new_job/', new_job, name='new_job'),
    path('available/', available_jobs, name='available_jobs'),
    path('new-message/', new_message, name='new_message'),
    path('new-quote/<int:job_id>/', new_quote, name='new_quote'),
]
