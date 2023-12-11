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
    path('edit_c/<int:pk>', EditComment.as_view(), name='edit_c'),
    path('del_c/<int:pk>', DelComment.as_view(), name='del_c'),
    path('del_user/<int:pk>', wanna_delete, name='wanna_delete'),
    path('delete_user/<int:pk>', delete_u_and_p, name='delete1'),

]