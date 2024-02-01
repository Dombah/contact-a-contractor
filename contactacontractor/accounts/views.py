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
    context = {
          'account': account,
          'jobs': jobs,
          'messages': messages,
    }
    return render(request, "accounts/user_dashboard.html", context)

def user_profile(request):
    account = Account.objects.get(user = request.user)
    context = {
          'account': account,
          'rating' : calculate_rating(request),
          'reviews' : Rating.objects.filter(ratee = request.user),
    }
    return render(request, "accounts/user_profile.html", context)

def calculate_rating(request):
    rating = Rating.objects.filter(ratee = request.user)
    total = 0
    for rate in rating:
        total += rate.rating
    return total / len(rating)