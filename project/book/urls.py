from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='reservas/signin.html'), name='login'),  # Changed name to 'login' (more conventional)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Reservas application URLs
    path('', views.IndexView.as_view(), name='index'),
    path('book/', views.book_table, name='book_table'),  
    path('my-bookings/', views.BookingListView.as_view(), name='booking_list')
]