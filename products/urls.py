from django.urls import path
from . import views

urlpatterns = [
    path('medicine/', views.MedicineDetails.as_view()),
    path('seed/', views.SeedDetails.as_view()),
    path('feed/', views.FeedDetails.as_view()),
    path('oil/', views.OilDetails.as_view()),
    path('miscellaneous/', views.MiscellaneousDetails.as_view()),
    path('repair/', views.RepairDetails.as_view())
]
