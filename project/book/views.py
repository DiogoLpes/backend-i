from datetime import timezone
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from book.models import Booking
from .forms import BookingForm
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

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
    
def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if request.user.is_authenticated:
                booking.email = request.user.email
                messages.success(request, 'Reserva efetuada com sucesso!')
            else:
                messages.success(request, 'Reserva efetuada como convidado! Crie uma conta para gerir suas reservas.')
            booking.save()
            return redirect('index')
    else:
        form = BookingForm()
    
    return render(request, 'reservas/index.html', {'form': form})



class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'book/booking_list.html'
    context_object_name = 'bookings'
    
    def get_queryset(self):
        return Booking.objects.filter(
            email=self.request.user.email,
            date__gte=timezone.now().date()
        ).order_by('date', 'time')