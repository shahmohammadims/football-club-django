from django.urls import path, include
from django.contrib.auth.views import LoginView , LogoutView , PasswordChangeView
from django.views.generic import TemplateView
from . import views
from .api.urls import urlpatterns

app_name = 'account'

urlpatterns = [
    path('' , TemplateView.as_view(template_name='home.html') , name='home'),
    path('profile/' , views.ProfileView.as_view() , name='profile'),
    path('login/' , LoginView.as_view(redirect_authenticated_user=True,next_page='account:profile'),name='login'),
    path('logout/' , LogoutView.as_view(next_page='/') , name='logout'),
    path('change-password/' , PasswordChangeView.as_view(success_url='account:profile',template_name='account/password_change_form.html') , name='change_password'),
    path('api/', include(urlpatterns))
]
