from django.urls import path
from Finanace import views

urlpatterns = [
    path('feepay/', views.fee_pay),
    path('feepaid/', views.fee_paid),
    path('feedue/', views.fee_due),
]