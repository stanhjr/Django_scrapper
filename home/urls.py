from django.urls import path


from . import views


urlpatterns = [
    path('get_data/', views.GetDataAPIView.as_view(), name='get_data'),
    path('login/', views.Login.as_view(), name='login'),
    path('', views.IndexView.as_view(), name='index'),
]