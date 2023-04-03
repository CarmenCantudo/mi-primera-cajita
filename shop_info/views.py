from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


def about_us(request):
    """ About us page """

    return render(request, 'shop_info/about_us.html')


def privacy_policy(request):
    """ Privacy Policy page """

    return render(request, 'shop_info/privacy_policy.html')


def cookie_policy(request):
    """ Cookie Policy page """

    return render(request, 'shop_info/cookie_policy.html')


def terms(request):
    """ Cookie Policy page """

    return render(request, 'shop_info/terms.html')


def faqs(request):
    """ Cookie Policy page """

    return render(request, 'shop_info/faqs.html')
