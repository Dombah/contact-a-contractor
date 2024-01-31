from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from app.admin import Account, Job, Quote, Dispute, Message, Rating

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
    return render(request, "accounts/register.html", context)

def user_dashboard(request):
    account = Account.objects.get(user = request.user)
    jobs = [job for job in Job.objects.all() if job.user.username == request.user.username]
    messages = [message for message in Message.objects.all() if message.receiver.username == request.user.username]
    your_quotes = [quote for quote in Quote.objects.all() if quote.contractor.username == request.user.username]
    your_job_quotes = [quote for quote in Quote.objects.all() if quote.job.user.username == request.user.username]
    context = {
          'account': account,
          'jobs': jobs,
          'messages': messages,
          'your_quotes': your_quotes,
          'your_job_quotes': your_job_quotes,
    }
    return render(request, "accounts/user_dashboard.html", context)

def user_profile(request):
    account = Account.objects.get(user = request.user)
    submitted_jobs = [quote.job for quote in Quote.objects.all() if quote.contractor.username == request.user.username]
    context = {
          'account': account,
          'submitted_jobs': submitted_jobs,
    }
    return render(request, "accounts/user_profile.html", context)