from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from reservas import views

urlpatterns = [
    
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='reservas/signin.html'), name='signin'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.IndexView.as_view(), name='index'),
]