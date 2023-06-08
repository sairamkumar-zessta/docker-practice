from django.urls import path
from Admissions import views

urlpatterns = [
    path('add/', views.add_admission),
    path('rep/', views.admission_report)
]