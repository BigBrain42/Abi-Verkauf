from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('order/create/', views.create_order, name='create_order'),
    path('seller/dashboard/', views.seller_dashboard, name='seller_dashboard'),
]
