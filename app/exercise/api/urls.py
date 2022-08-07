from django.urls import path, include
from . import views

urlpatterns = [
    path('category/', include([
        path('',views.CategoryList.as_view()),
        path('<pk>',views.CategoryDetail.as_view()),
    ]))
]
