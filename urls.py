from django.urls import path
from . import views

urlpatterns = [
    path('', views.lead_list, name='lead_list'),
    path('lead/<int:id>/', views.lead_detail, name='lead_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
]