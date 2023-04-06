from django.contrib import admin
from .models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    """ Contact Us messages """
    list_display = (
        'name',
        'email',
        'subject',
        'message',
        'date_submitted',
    )
    ordering = ('date_submitted',)


admin.site.register(ContactUs, ContactUsAdmin)
