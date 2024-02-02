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
    assigned_jobs = [quote.job for quote in Quote.objects.all() if quote.accepted == True and quote.contractor.username == request.user.username and not quote.job.is_completed]
    completed_jobs = Job.objects.filter(user=request.user, is_completed=True)
    completed_Contractor_Jobs = completed_Contractor_Jobs = Job.objects.filter(quote__contractor=request.user, is_completed=True)     
    context = {
          'account': account,
          'jobs': jobs,
          'messages': messages,
          'your_quotes': your_quotes,
          'your_job_quotes': your_job_quotes,
          'assigned_jobs': assigned_jobs,
          'completed_jobs': completed_jobs,
          'completed_Contractor_Jobs': completed_Contractor_Jobs,
          'JOB_STATUS_AVAILABLE': Job.JOB_STATUS_AVAILABLE,
          'JOB_STATUS_ACCEPTED': Job.JOB_STATUS_ACCEPTED,
          'JOB_STATUS_IN_PROGRESS': Job.JOB_STATUS_IN_PROGRESS,
    }
    return render(request, "accounts/user_dashboard.html", context)

def contractor_profile(request, username):
    account = Account.objects.get(user__username=username)
    is_Owner = account.user == request.user

    if(request.method == "POST"):
        form_type = request.POST.get("form_type", None)
        if(form_type == "start_Job"):
            setJobInProgress(request.POST.get("job_id"))
        elif(form_type == "complete_Job"):
            job_id = request.POST.get("job_id")
            setJobComplete(job_id)
            updateContractorBalance(Quote.objects.get(job_id = job_id).id)
    
    assigned_jobs = [quote.job for quote in Quote.objects.all() if quote.accepted == True and quote.contractor.username == request.user.username and not quote.job.is_completed]
    completed_Contractor_Jobs = completed_Contractor_Jobs = Job.objects.filter(quote__contractor=account.user, is_completed=True)
    reviews = Rating.objects.filter(ratee = account.user) 
    context = {
        'account': account,
        'is_Owner': is_Owner,
        'completed_Contractor_Jobs': completed_Contractor_Jobs,
        'assigned_jobs': assigned_jobs,
        'rating' : calculate_rating(request),
        'reviews' : reviews,
        'max_Rating_Range' : range(5),
        'JOB_STATUS_IN_PROGRESS': Job.JOB_STATUS_IN_PROGRESS,
        'JOB_STATUS_ACCEPTED': Job.JOB_STATUS_ACCEPTED,
    }
    return render(request, "accounts/contractor_profile.html", context)

def user_profile(request, username):
    account = Account.objects.get(user__username=username)
    is_Owner = account.user == request.user
    completed_jobs = [job for job in Job.objects.all() if job.user.username == account.user.username and job.is_completed == True]
    if(is_Owner):
        accepted_jobs = [job for job in Job.objects.all() if job.user.username == request.user.username and job.status == "accepted"]
        context = {
            'account': account,
            'accepted_jobs': accepted_jobs,
            'completed_jobs': completed_jobs,
            'is_Owner': is_Owner,
        }
        return render(request, "accounts/user_profile.html", context)
    else:
        done_jobs = [quote.job for quote in Quote.objects.all() if quote.job.is_completed == True and quote.contractor.username == account.user.username]
        context = {
            'account': account,
            'completed_jobs': completed_jobs,
            'is_Owner': is_Owner,
        }
        return render(request, "accounts/user_profile.html", context)

def become_contractor(request):
    if request.method == "POST":
          account = Account.objects.get(user = request.user)
          account.contractor = True
          account.save()
          return HttpResponseRedirect(
                     redirect_to= '/accounts/dashboard/'
            )
    context = {}
    return render(request, "accounts/become_contractor.html", context)

def new_reply(request, message_id):
      if request.method == "POST":
            sender = request.user
            receiver = Message.objects.get(id = message_id).sender
            text = request.POST.get("message")

            message = Message(sender = sender, receiver = receiver, text = text)
            message.save()

            return HttpResponseRedirect(
                  redirect_to= '/'
            )
      context = {
            'subject': Message.objects.get(id = message_id).sender.username,
      }
      return render(request, 'accounts/new_reply.html', context)

def calculate_rating(request):
    rating = Rating.objects.filter(ratee = request.user)
    total = 0
    for rate in rating:
        total += rate.rating
    if len(rating) == 0:
        return 0
    return round(total / len(rating), 2)

def confirm_quote(request, quote_id):
      if request.method == "POST":
           quote = Quote.objects.get(id = quote_id)
           quote.accepted = True
           quote.job.status = "assigned"
           quote.job.save()
           quote.save()
           return HttpResponseRedirect(
                 redirect_to= '/accounts/dashboard/'
           )
      context = {}
      return render(request, 'accounts/confirm_quote.html', context)

def setJobInProgress(job_id):
    job = Job.objects.get(id = job_id)
    job.status = Job.JOB_STATUS_IN_PROGRESS
    job.save()

def setJobComplete(job_id):
    job = Job.objects.get(id = job_id)
    job.status = Job.JOB_STATUS_COMPLETE
    job.is_completed = True
    job.save()

def updateContractorBalance(quote_id):
    quote = Quote.objects.get(id = quote_id)
    contractor_Account = Account.objects.get(user = quote.contractor)
    contractor_Account.balance += quote.price
    contractor_Account.save()
    
def job_status(request, job_id):
    job = Job.objects.get(id = job_id)
    context = {
        'job': job,
        'JOB_STATUS_AVAILABLE': Job.JOB_STATUS_AVAILABLE,
        'JOB_STATUS_ACCEPTED': Job.JOB_STATUS_ACCEPTED,
        'JOB_STATUS_IN_PROGRESS': Job.JOB_STATUS_IN_PROGRESS,
    }
    return render(request, "accounts/job_status.html", context)

def contract_status(request, job_id):
    job = Job.objects.get(id = job_id)
    context = {
        'job': job,
        'JOB_STATUS_AVAILABLE': Job.JOB_STATUS_AVAILABLE,
        'JOB_STATUS_ACCEPTED': Job.JOB_STATUS_ACCEPTED,
        'JOB_STATUS_IN_PROGRESS': Job.JOB_STATUS_IN_PROGRESS,
    }
    return render(request, "accounts/job_status.html", context)