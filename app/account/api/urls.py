from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccountList.as_view())
]
