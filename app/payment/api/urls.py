from xml.etree.ElementInclude import include
from django.urls import path , include
from . import views
urlpatterns = [
    path('', views.PaymentList.as_view()),
    path('<pk>/', views.PaymentDetail.as_view()),
]
