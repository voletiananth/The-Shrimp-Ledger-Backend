from django.urls import path
from . import views

urlpatterns = [
    path('seasons/', views.SeasonApiView.as_view())
]
