from django.shortcuts import render
from django.contrib.auth.models import User
from app.models import Account, Job, Dispute, Message, Rating
from django.http import HttpResponseRedirect

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
                  redirect_to= '/accounts/dashboard/'
            )
      context = {}
      return render(request, 'app/new_job.html', context)


def submit_dispute(request, job_id):
    if request.method == "POST":
            user = request.user
            job = Job.objects.get(id = job_id)
            reason = request.POST.get("dispute")

            dispute = Dispute(user = user, job = job, reason = reason)
            dispute.save()
            return HttpResponseRedirect(
                  redirect_to= '/accounts/dashboard/'
            )
    context = {}
    return render(request, 'app/submit_dispute.html', context)

def submit_review(request, job_id):
    if request.method == "POST":
            rater = request.user
            job = Job.objects.get(id = job_id)
            ratee = job.user
            review = request.POST.get("message")
            rating = request.POST.get("rating")

            rating = Rating(rater = rater, ratee = ratee, job = job, review = review, rating = rating)
            rating.save()
            return HttpResponseRedirect(
                  redirect_to= '/accounts/dashboard/'
            )
    context = {}
    return render(request, 'app/submit_review.html', context)

def available_jobs(request):
      account = Account.objects.get(user=request.user)
      available_jobs = [job for job in Job.objects.all() if job.status == "available"]
      context = {
            'account': account,
            'available_jobs': available_jobs,
      }
      return render(request, 'app/available_jobs.html', context)

def new_message(request):
      if request.method == "POST":
            sender = request.user
            receiver = User.objects.get(username=request.POST.get("receiver"))
            text = request.POST.get("message")

            message = Message(sender = sender, receiver = receiver, text = text)
            message.save()

            return HttpResponseRedirect(
                  redirect_to= '/'
            )
      context = {}
      return render(request, 'app/new_message.html', context)
