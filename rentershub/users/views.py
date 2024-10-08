from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate


#A view for creating a new user
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        valid = super(SignUpView, self).form_valid(form)
        email, password = form.cleaned_data.get('email'), form.cleaned_data.get('password1')
        user = form.save()
        login(self.request, user, backend='users.backend.EmailPhoneAuthenticationBackend')
        return valid

#A view for displaying the home page
class HomeView(TemplateView):
    template_name = 'main.html'

