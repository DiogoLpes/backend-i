from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.urls import reverse_lazy
from .forms import ReservationForm
from .models import Reservation

class ReservationListView(LoginRequiredMixin, CreateView):
    login_url = "/signin"
    success_url = reverse_lazy("reservation_list")
    form_class = ReservationForm
    template_name = "reservations/list.html"

    def get_context_data(self, **kwargs):
        kwargs['reservations'] = Reservation.objects.filter(user=self.request.user).all()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class IndexView(TemplateView):
    http_method_names = ['get']
    template_name = "reservations/index.html"

class SignUpView(FormView):
    template_name = "reservations/signup.html"
    success_url = reverse_lazy("reservation_list")
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")