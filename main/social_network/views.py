from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from social_network.forms import RegistrationForm


# Create your views here.

def index(request):
    return render(request, 'social_network/index.html', context={'title':'Главная страница'})

class Registration(CreateView):
    form_class = RegistrationForm
    template_name = 'social_network/registration.html'
    extra_context = {
        'title':'Создание пользователя'
    }
    success_url = reverse_lazy('main:login')


class LoginViewMy(LoginView):
    form_class = AuthenticationForm
    template_name = 'social_network/login.html'
    extra_context = {'title':'Авторизация'}