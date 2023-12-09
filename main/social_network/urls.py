from django.urls import path, include
from .views import *

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('registration/', Registration.as_view(), name='registration'),
    path('login/', LoginViewMy.as_view(), name='login'),

]