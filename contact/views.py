from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


# Create your views here.
def contact(request):
    if request.method == "POST":

        message_name = request.POST.get('name')
        message_subject = request.POST.get('subject')
        message_email = request.POST.get('email')
        message_message = request.POST.get('message')

        data = {
            'name': message_name,
            'subject': message_subject,
            'email': message_email,
            'message': message_message
        }

        message = """
        From: {}
        New message: {}
        Email: {}
        """.format(data['name'], data['message'], data['email'])
        # send an email
        send_mail(data['subject'], message, '', ['mpt.craig@gmail.com'])
        messages.success(request, f'Your email was send Successfully!')

        return render(request, 'contact/contact.html', {})
    else:
        return render(request, 'contact/contact.html', {})
