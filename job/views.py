from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class JobCreateView(LoginRequiredMixin, CreateView):
    model = models.Job
    fields = "__all__"
    success_url = "/"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
        
class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Job
    fields = "__all__"
    success_url = "/"  

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
                
class JobDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Job
    success_url = "/"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
        
class JobListView(ListView):
    model = models.Job
    
class JobDetailView(LoginRequiredMixin, DetailView):
    model = models.Job    
 
class RegisterView(CreateView):
    model = models.Job
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = "/login"
