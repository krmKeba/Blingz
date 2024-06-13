from . import views
from django.urls import path

urlpatterns = [
    path('app_1/', views.app_1, name='app_1'),
]