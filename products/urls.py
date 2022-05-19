from django.urls import path
from . import views

urlpatterns = [
    path('medicines/', views.MedicineDetails.as_view())
]
