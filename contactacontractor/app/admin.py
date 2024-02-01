from django.contrib import admin

from app.models import Account, Job, Quote, Dispute, Rating, Message


class DisputeAdmin(admin.ModelAdmin):
    readonly_fields = ['user', 'job', 'reason']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True
    
class JobAdmin(admin.ModelAdmin):
    readonly_fields = ['user', 'title', 'description', 'location', 'type', 'budget']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(Dispute, DisputeAdmin)
admin.site.register(Account)
admin.site.register(Job, JobAdmin)
admin.site.register(Quote)
admin.site.register(Message)
admin.site.register(Rating)