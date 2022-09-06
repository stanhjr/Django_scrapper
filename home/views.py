import time

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login as auth_login

from home.forms import LoginForm
from home.models import OlxModel
from home.serializers import OlxSerializer
from home.tools import start_parser


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = reverse_lazy('login')


class Login(LoginView):
    success_url = reverse_lazy('index')
    form_class = LoginForm
    template_name = 'login.html'

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'username or password fields does not match')
        return redirect(reverse_lazy('login'))

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.user)
        return HttpResponseRedirect(reverse_lazy('index'))


class GetDataAPIView(APIView):
    def get(self, request):
        # OlxModel.objects.all().delete()
        print(request.user)
        count_items = self.request.user.get_number_items()
        print(count_items)
        # start_parser(count_items)
        content = render_to_string(
            "product_list.html",
            request=request,
            context={
                'products': OlxModel.objects.all()[:count_items]
            }
        )
        # s = OlxSerializer(instance=OlxModel.objects.all()[:100], many=True)
        return Response({"content": content})


class FilterDataAPIView(APIView):
    def get(self, request):
        count_items = self.request.user.get_number_items()
        if self.request.query_params.get('order') == 'up':
            products = OlxModel.objects.order_by("-price_grv").all()[:count_items]
        elif self.request.query_params.get('order') == 'down':
            products = OlxModel.objects.order_by("price_grv").all()[:count_items]
        else:
            products = OlxModel.objects.order_by("price_grv").all()[:count_items]
        content = render_to_string(
            "product_list.html",
            request=request,
            context={
                'products': products
            }
        )
        return Response({"content": content})


class ProductDetail(APIView):
    """
    Delete a product instance.
    """

    def get_object(self, pk):
        try:
            return OlxModel.objects.get(pk=pk)
        except OlxModel.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
