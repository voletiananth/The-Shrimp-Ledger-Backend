from django.urls import path
from . import views

urlpatterns = [
    path('season/', views.SeasonApiView.as_view()),
    path('transaction/', views.TransactionApiView.as_view())
]
