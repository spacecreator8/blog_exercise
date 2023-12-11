from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from social_network.forms import RegistrationForm, CommentsForm, UpdateForm
from social_network.models import Profile, User


# Create your views here.

def index(request):
    return render(request, 'social_network/index.html', context={'title': 'Главная страница'})


class Registration(CreateView):
    form_class = RegistrationForm
    template_name = 'social_network/registration.html'
    extra_context = {
        'title': 'Создание пользователя'
    }
    success_url = reverse_lazy('main:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        profile = Profile.objects.create()
        user.page = profile
        user.save()
        return response


class LoginViewMy(LoginView):
    form_class = AuthenticationForm
    template_name = 'social_network/login.html'
    extra_context = {'title': 'Авторизация'}
    success_url = reverse_lazy('main:index')


@login_required
def page_with_message(request, pk):
    user_object = get_user_model().objects.get(pk=pk)
    page_object = user_object.page

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.username = user_object
            f.page = page_object
            f.save()
    else:
        form = CommentsForm()

    message_q = page_object.message_set.all()
    context = {
        'user_object': user_object,
        'page_object': page_object,
        'message_q': message_q,
        'form': form,
        'title': user_object.username
    }
    return render(request, 'social_network/page.html', context=context)


@login_required
def update_page(request, pk):
    if pk == request.user.pk:
        if request.method == 'POST':
            form = UpdateForm(request.POST, request.FILES)
            if form.is_valid():
                cd = form.cleaned_data
                user = get_user_model().objects.get(pk=pk)
                user.first_name = cd['first_name']
                user.last_name = cd['last_name']
                user.image = cd['image']
                user.save()

                profile = Profile.objects.get(pk=pk)
                profile.status = cd['status']
                profile.date_birth = cd['date_birth']
                profile.about = cd['about']
                profile.save()
                # get_user_model().objects.update(cd['first_name'], cd['last_name'], cd['image'])
                # Profile.objects.update(cd['status'], cd['date_birth'], cd['about'])
        else:
            stub = get_user_model().objects.get(pk=pk).first_name
            stub2 = get_user_model().objects.get(pk=pk).last_name
            stub3 = get_user_model().objects.get(pk=pk).image
            stub4 = Profile.objects.get(pk=pk).status
            stub5 = Profile.objects.get(pk=pk).date_birth
            stub6 = Profile.objects.get(pk=pk).about

            dict1 = {
                'first_name': stub,
                'last_name': stub2,
                'image': stub3,
                'status': stub4,
                'date_birth': stub5,
                'about': stub6
            }
            form = UpdateForm(initial=dict1)
        context = {
            'form': form,
            'title': 'Редактирование данных'
        }
        return render(request, 'social_network/update.html', context=context)
    else:
        return redirect('/')
