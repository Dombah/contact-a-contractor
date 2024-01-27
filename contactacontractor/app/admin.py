from django.contrib import admin

from app.models import Account, Job, Quote, Dispute, Rating, Message

admin.site.register(Account)
admin.site.register(Job)
admin.site.register(Quote)
admin.site.register(Dispute)
admin.site.register(Message)
admin.site.register(Rating)