from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.product_home, name='product_home'),
    path('mobile/', include('mobile.urls')),
]