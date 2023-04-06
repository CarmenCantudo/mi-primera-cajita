from django.db import models
from django.utils import timezone


class ContactUs(models.Model):
    name = models.CharField(max_length=125)
    email = models.EmailField(max_length=125)
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=1000)
    date_submitted = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Contact Us'
        ordering = ['-date_submitted']

    def __str__(self):
        return self.subject
