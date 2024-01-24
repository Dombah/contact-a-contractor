from django.contrib import admin

from app.models import Account, Job, Quote

# Register your models here.
admin.site.register(Account)
admin.site.register(Job)
admin.site.register(Quote)