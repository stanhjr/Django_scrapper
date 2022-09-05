from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib import messages
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from home.forms import LoginForm


class IndexView(TemplateView):
    template_name = 'index.html'


class Login(LoginView):
    success_url = '/'
    form_class = LoginForm
    template_name = 'login.html'

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'username or password fields does not match')
        return redirect(reverse_lazy('login'))


class GetDataAPIView(APIView):
    def get(self, request):
        response = {"re": "123"}
        return Response(response)
