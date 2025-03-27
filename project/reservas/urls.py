from django.urls import path
from django.contrib.auth.views import LoginView
from reservas import views

urlpatterns = [
    path("reservations", views.ReservationListView.as_view(), name="reservation_list"),
    path("reservation/new", views.CreateReservationView.as_view(), name="create_reservation"),
    path("reservation/edit/<int:pk>", views.UpdateReservationView.as_view(), name="edit_reservation"),
    path("reservation/cancel/<int:pk>", views.CancelReservationView.as_view(), name="cancel_reservation"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("signin", LoginView.as_view(template_name="reservas/signin.html"), name="signin"),
    path("logout", views.logout_view, name="logout"),
    path("", views.IndexView.as_view(), name="index"),
]