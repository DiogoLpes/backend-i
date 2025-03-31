from datetime import timezone
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from reservas.models import Booking
from .forms import BookingForm
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as AuthLoginView

class IndexView(TemplateView):
    template_name = "book/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookingForm()  # Add the form to the context
        return context

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class LoginView(AuthLoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return redirect('book/index')


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
    
def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if request.user.is_authenticated:
                booking.email = request.user.email
                booking.save()
                messages.success(request, 'Reserva efetuada com sucesso!')
                return redirect('booking_list') 
            else:
                booking.save()
                return redirect('index')
    else:
        form = BookingForm()
    
    return render(request, 'book/index.html', {'form': form})



class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'book/booking_list.html'
    context_object_name = 'bookings'
    
    def get_queryset(self):
        return Booking.objects.all()