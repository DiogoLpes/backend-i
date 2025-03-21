from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,TemplateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin


from todo.models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request,"todo/index.html", {"foo":"World", "tasks": tasks})

class TaskListView(LoginRequiredMixin, ListView):
    login_url = "/signin"
    model = Task


    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).all()

class IndexView(TemplateView):
    http_method_names = ['get']
    template_name = "todo/index.html"

class SignupView(FormView):
    Template_name= "registration/signup.html"
    sucess_url = "/" 
    form_class = UserCreationForm
     
    def from_valid(self, form):
        form.save()
        return super().form_valid(form)

        