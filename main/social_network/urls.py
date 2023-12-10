from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .views import *

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('registration/', Registration.as_view(), name='registration'),
    path('login/', LoginViewMy.as_view(), name='login'),
    path('profile/<int:pk>', page_with_message, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update/<int:pk>', update_page, name='update'),

]