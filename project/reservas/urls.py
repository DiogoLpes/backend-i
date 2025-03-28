from django.urls import path
from django.urls import path
from .views import ReservationListView, IndexView, SignUpView, logout_view
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("reservations/", ReservationListView.as_view(), name="reservation_list"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signin/", LoginView.as_view(template_name="reservations/signin.html"), name="signin"),
    path("logout/", logout_view, name="logout"),
]