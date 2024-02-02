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
from accounts.views import register, user_dashboard, user_profile, become_contractor, new_reply, confirm_quote, job_status, contract_status
from app.views import submit_dispute, submit_review, view_quotes

app_name = "accounts"
urlpatterns = [
    path('register/', register, name='register'),
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('profile/<str:username>', user_profile, name='user_profile'),
    path('dashboard/submit-dispute/<int:job_id>/', submit_dispute, name='submit_dispute'),
    path('dashboard/submit-review/<int:job_id>/', submit_review, name='submit_review'),
    path('dashboard/view-quotes/<int:job_id>/', view_quotes, name='view_quotes'),
    path('become-contractor/', become_contractor, name='become_contractor'),
    path('dashboard/new-reply/<int:message_id>/', new_reply, name='new_reply'),
    path('dashboard/confirm-quote/<int:quote_id>/', confirm_quote, name='confirm_quote'),
    path('dashboard/job-status/<int:job_id>/', job_status, name='job_status'),
    path('dashboard/contract-status/<int:job_id>/', contract_status, name='contract_status')
]

