from django.urls import path
from django.contrib.auth.views import LoginView , LogoutView

app_name = 'account'

urlpatterns = [
    path('login/' , LoginView.as_view(redirect_authenticated_user=True,next_page='/'),name='login'),
    path('logout/' , LogoutView.as_view()),
]
