from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_message = request.POST['message']

        # send an email

        

        context = {
            'name': message_name,
        }

        return render(request, 'contact/contact.html', context)
    else:
        return render(request, 'contact/contact.html', {})