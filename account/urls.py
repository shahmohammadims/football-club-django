from django.urls import path
from django.contrib.auth.views import LoginView , LogoutView , PasswordChangeView
from . import views
app_name = 'account'

urlpatterns = [
    path('profile/' , views.ProfileView.as_view() , name='profile'),
    path('login/' , LoginView.as_view(redirect_authenticated_user=True,next_page='account:profile'),name='login'),
    path('logout/' , LogoutView.as_view() , name='logout'),
    path('change-password/' , PasswordChangeView.as_view(success_url='account:profile') , name='change_password')
]
