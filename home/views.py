from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
# Create your views here.


def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email_from = settings.EMAIL_HOST_USER
        recepient_list = [email]
        html_message = render_to_string(
            'email.html', {'message': message})
        send_mail(subject, message, email_from,
                  recepient_list, html_message=html_message)
        return redirect('/sent')
    return render(request, 'home.html')


def email_sent(request):
    return render(request, 'sent.html')
