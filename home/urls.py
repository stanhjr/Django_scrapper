from django.urls import path


from . import views


urlpatterns = [
    path('get_data/', views.GetDataAPIView.as_view(), name='get_data'),
    path('filter_data/', views.FilterDataAPIView.as_view(), name='filter_data'),
    path('login/', views.Login.as_view(), name='login'),
    path('delete_item/<int:pk>/', views.ProductDetail.as_view(), name='delete_item'),
    path('', views.IndexView.as_view(), name='index'),
]