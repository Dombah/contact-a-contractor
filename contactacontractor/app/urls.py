from django.urls import path
from .views import new_job, submit_dispute

urlpatterns = [
    path('new/', new_job, name='new_job'),
]
