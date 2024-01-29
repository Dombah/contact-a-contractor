from django.shortcuts import render
from django.contrib.auth.models import User
from app.models import Account, Job
from django.http import HttpResponseRedirect

def home(request):
    context = {}
    return render(request, "app/home.html", context)

def register(request):
    if request.method == "POST":
                username = request.POST.get("username")
                first_name = request.POST.get("first_name")
                last_name = request.POST.get("last_name")
                email = request.POST.get("email")
                password = request.POST.get("password")
                contractor = request.POST.get("contractor")

                user = User.objects.create_user(username = username, password = password, email = email, first_name = first_name, last_name = last_name)
                user.save()

                account = Account(user = user, first_name = first_name, last_name = last_name, balance = 0, contractor = True if contractor == "on" else False)
                account.save()
                return HttpResponseRedirect(
                       redirect_to= '/'
                )
    context = {}
    return render(request, "registration/register.html", context)

def user_dashboard(request):
    account = Account.objects.get(user = request.user)
    jobs = [job for job in Job.objects.all() if job.user.username == request.user.username]
    context = {
          'account': account,
          'jobs': jobs
    }
    return render(request, "registration/user_dashboard.html", context)

def user_profile(request):
    account = Account.objects.get(user = request.user)
    context = {
          'account': account
    }
    return render(request, "registration/user_profile.html", context)

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
                  redirect_to= '/account/user_dashboard/'
            )
      context = {}
      return render(request, 'app/new_job.html', context)