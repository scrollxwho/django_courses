from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
# Create your views here.
from .models import Course


def index(request):

    # return HttpResponse("What's up?")
    return render(request, 'home/index.html')

def pricing(request):

    # return HttpResponse("What's up?")
    return render(request, 'home/pricing.html')

class RegisterUser(CreateView):
    template_name = 'home/registration.html'
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
    template_name = 'home/login.html'
    form_class = AuthenticationForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context
    def get_success_url(self):
        return reverse_lazy('index')

class UsersView(ListView):
    template_name = 'home/users.html'
    model = User
    context_object_name = 'users'


def checkcourses(requests):
    print(Course.objects.all())

    return redirect('/')






