from django.urls import path, include
from .views import RegisterApi
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', RegisterApi.as_view()),
    path('login/', jwt_views.TokenObtainPairView.as_view()),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view())
]
