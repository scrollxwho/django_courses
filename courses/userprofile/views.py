from django.shortcuts import render
import ssl

from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.core.mail import send_mail
import smtplib
from email.message import EmailMessage
from django.contrib import messages

def profile(request):

    return render(request, 'userprofile/profile.html')


class RegisterUser(CreateView):
    template_name = 'userprofile/registration.html'
    form_class = RegisterForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'register'
        return context
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

    # def get_queryset(self):
    #     return User.objects.all()

def exit(request):
    logout(request)

    return redirect('registration')

class UsersLoginView(LoginView):
    template_name = 'userprofile/login.html'
    form_class = AuthenticationForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context
    def get_success_url(self):
        return reverse_lazy('index')

class UsersView(ListView):
    template_name = 'userprofile/users.html'
    model = User
    context_object_name = 'users'

class SendEmail(View):
    def get(self, request):
        # topic = 'Тестове повідомлення'
        # message = 'Привіт!'
        # email_from = settings.EMAIL_HOST_USER
        # email_to = ['gsmkibernetik@gmail.com']
        # send_mail(topic, message, email_from, email_to)
        #

        # msg = EmailMessage()
        # msg.set_content("Текст повідомлення")
        # msg["Subject"] = "Тема листа"
        # msg["From"] = settings.EMAIL_HOST_USER
        # msg["To"] = 'gsmkibernetik@gmail.com'
        #
        # context = ssl.create_default_context()
        #
        # with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
        #     smtp.starttls(context=context)
        #     smtp.login(msg["From"], settings.EMAIL_HOST_PASSWORD)
        #     smtp.send_message(msg)



        message = """\
                What's up?."""

        server = smtplib.SMTP(settings.EMAIL_HOST, 587)
        server.ehlo()  # Can be omitted
        server.starttls(context=ssl.create_default_context())  # Secure the connection
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        server.sendmail("maksnoname58@gmail.com", "dhejrrhjrjr@gmail.com", f"Subject: {message}")
        server.quit()

        return HttpResponse("Повідомлення відправлено")
