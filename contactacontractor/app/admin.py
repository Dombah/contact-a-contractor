from django.contrib import admin

from app.models import Account, Job, Quote
from app.models import Account, Job, Dispute

# Register your models here.
admin.site.register(Account)
admin.site.register(Job)
admin.site.register(Quote)
admin.site.register(Dispute)
