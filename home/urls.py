from django.urls import path


from . import views


urlpatterns = [
    path('login/', views.LoginPage.as_view(), name='login'),

]