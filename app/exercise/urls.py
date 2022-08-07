from django.urls import path,include
from .api.urls import urlpatterns

app_name = 'exercise'

urlpatterns = [
    path('api/', include(urlpatterns))
]