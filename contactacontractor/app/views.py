from django.shortcuts import render
from django.contrib.auth.models import User
from app.models import Account, Job, Dispute
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
    context = {}
    return render(request, "app/home.html", context)

def new_job(request):
      if request.method == "POST":
            user = request.user
            title = request.POST.get("title")
            description = request.POST.get("description")
            location = request.POST.get("location")
            type = request.POST.get("type")
            budget = request.POST.get("budget")
            is_completed = False

            job = Job(user = user, title = title, description = description, location = location, type = type, budget = budget, is_completed = is_completed)
            job.save()

            return HttpResponseRedirect(
                  redirect_to= '/accounts/user_dashboard/'
            )
      context = {}
      return render(request, 'app/new_job.html', context)


def submit_dispute(request, user, job_id):
    if request.method == "POST":
            user = request.user
            job = Job.objects.get(id = job_id)
            reason = request.POST.get("dispute")

            dispute = Dispute(user = user, job = job, reason = reason)
            dispute.save()
            return HttpResponseRedirect(
                  redirect_to= '/accounts/user_dashboard/'
            )
    context = {}
    return render(request, 'app/submit_dispute.html', context)