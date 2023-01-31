from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

class TokenCreateView(TokenObtainPairView):
    pass

class TokenRefreshView(TokenRefreshView):
    pass