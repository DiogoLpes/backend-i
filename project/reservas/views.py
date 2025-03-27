from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView, CreateView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from .forms import ReservationForm
from .models import Reservation, Table

class ReservationListView(LoginRequiredMixin, CreateView):
    login_url = "/login"
    success_url = "/reservations"
    form_class = ReservationForm
    template_name = "reservations/base.html"

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Reservation.objects.filter(customer=self.request.user).all()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)

class HomeView(TemplateView):
    http_method_names = ['get']
    template_name = "reservations/reservation_list.html"

class SignUpView(FormView):
    template_name = "registration/signup.html"
    success_url = "/reservations"
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")