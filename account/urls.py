from django.urls import path
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from .views import profile

app_name = 'account'

urlpatterns = [
    path('profile/' , profile , name='profile'),
    path('login/' , LoginView.as_view(template_name='admin/login.html',next_page='account:profile' , redirect_authenticated_user=True) , name='login')
]
