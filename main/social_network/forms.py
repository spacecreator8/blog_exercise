from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from social_network.models import Message


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    password1 = forms.CharField(label='Придумайте пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'image']

        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'image': 'Аватарка',
            'email': 'Ваша почта'
        }


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 100, 'rows': 5, 'placeholder': 'Сообщение'})
        }
        labels = {
            'text': 'Оставить сообщение',
        }

    def clean_text(self):
        cd = self.cleaned_data
        if cd['text'] == '' or cd['text'] == ' ':
            raise forms.ValidationError('Комментарий не должен быть пустым.')
        return cd['text']
