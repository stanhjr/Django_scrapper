from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib import messages

from home.forms import LoginForm


# class LoginPage(TemplateView):
#     template_name = 'login.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['login_form'] = LoginForm
#         return context


class Login(LoginView):
    success_url = '/'
    form_class = LoginForm
    template_name = 'login.html'

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'username or password fields does not match')
        return redirect(reverse_lazy('login'))
