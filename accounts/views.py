from django.shortcuts import render, redirect
# from django.
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.models import auth
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.


def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        graduation_year = request.POST['graduation_year']
        course_name = request.POST['course_name']
        GR_number = request.POST['GR_number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if CustomUser.objects.filter(email=email).exists():
                return redirect('/')
            else:
                user = CustomUser.objects.create_user(
                    name=name, email=email, graduation_year=graduation_year, course_name=course_name, GR_number=GR_number, password=password1)
                user.save()
                #Email will  be sent here
                # mydict={'name':name}
                # html_template = 'register_email.html'
                # html_message = render_to_string(html_template, context=mydict)
                # subject = 'Welcome to AlumTrack'
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = [email]
                # message = EmailMessage(subject, html_message,email_from, recipient_list)
                # message.content_subtype = 'html'
                # message.send()
                return redirect('signin')

        else:
            print('password did not match')
            return redirect('/')
    else:
        return render(request, 'registration.html')


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Fill the data')
            return redirect('signin')

    else:
        return render(request, 'signin.html')
