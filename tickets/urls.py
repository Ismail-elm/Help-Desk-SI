# tickets/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_tickets, name='liste_tickets'),
    path('creer/', views.creer_ticket, name='creer_ticket'),
    path('<int:pk>/', views.detail_ticket, name='detail_ticket'),
    path('<int:pk>/statut/', views.modifier_statut, name='modifier_statut'),
    path('export/json/', views.export_json, name='export_json'),
]