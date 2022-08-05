from django.urls import path , include
from . import views
from .api.urls import urlpatterns

app_name = 'payment'

urlpatterns = [
    path('' , views.IndexView.as_view(), name='index'),
    path('api/', include(urlpatterns)),
]
