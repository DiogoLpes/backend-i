from django.contrib.auth.views import LoginView, LogoutView 
from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),  
    path('logout/', LogoutView.as_view(), name='logout'),

    # Reservas application URLs
    path('', views.IndexView.as_view(), name='index'),
    path('booking', views.book_table, name='book_table'),  
    path('user-bookings/', views.BookingListView.as_view(), name='booking_list')
]