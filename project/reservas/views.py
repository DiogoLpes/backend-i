from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.urls import reverse_lazy
from .forms import ReservationForm
from .models import Reservation


class IndexView(TemplateView):
    template_name = "reservas/index.html"

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('signin')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")