from django.contrib import admin

from .models import About_us, Worker, Clients, Contac, Feedback, Certificates


class About_usAdmin(admin.ModelAdmin):
    list_display = 'name', 'description', 'published'
    list_filter = 'published',
    list_editable = 'published',


class WorkerAdmin(admin.ModelAdmin):
    list_display = 'position', 'name', 'phone', 'email', 'published'
    list_filter = 'position',
    list_editable = 'name', 'phone', 'published'


class ClientsAdmin(admin.ModelAdmin):
    list_display = 'name', 'published'
    list_filter = 'name',
    list_editable = 'published',


class ContacAdmin(admin.ModelAdmin):
    list_display = 'name', 'address', 'time_work1', 'time_work2'
    list_editable = 'address', 'time_work1', 'time_work2'


class CertificatesAdmin(admin.ModelAdmin):
    list_display = 'name', 'published'
    list_editable = 'published',


class FeedbackAdmin(admin.ModelAdmin):
    list_display = 'name', 'phone', 'message', 'datetime', 'published'
    list_filter = 'name', 'phone', 'published'
    list_editable = 'published',


admin.site.register(About_us, About_usAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Clients, ClientsAdmin)
admin.site.register(Contac, ContacAdmin)
admin.site.register(Certificates, CertificatesAdmin)
admin.site.register(Feedback, FeedbackAdmin)
