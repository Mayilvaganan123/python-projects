from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_order, name='submit_order'),
    path('dashboard/',views.Dashboard, name='Dashboard'),
    path('', views.menu_view, name='menu'),
]