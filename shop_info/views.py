from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

from .forms import ContactUsForm


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


def contact_us(request, *args, **kwargs):
    """ Contact Us page """
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'],
            email = form.cleaned_data['email'],
            subject = form.cleaned_data['subject'],
            message = form.cleaned_data['message'],
            form.save()

            send_mail({subject}, f'{name}, {email}, {message}',
                      settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER],
                      fail_silently=False)
            messages.success(request,
                             f'Thank you for reaching out to us!'
                             f'We appreciate your interest and will get back '
                             f'to you as soon as possible.'
                             )

            return redirect(reverse('home'))
        else:
            messages.error(request,
                           f'Something went wrong sending your message.'
                           f'Please try again.'
                           )

    else:
        form = ContactUsForm()

    return render(request, 'shop_info/contact_us.html', {'form': form})
