from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.signup),
    re_path(r'(\d+)/', views.signup_detail),
]
