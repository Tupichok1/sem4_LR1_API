from django.urls import path, re_path, include
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('registration', views.RegistrView.as_view(), name = "registration"),
    path('auth', obtain_auth_token, name='api-token-auth'),
    path('logout', views.Logout.as_view(), name = "Logout"),
    path('takeToken', views.takeToken.as_view(), name = "TakeToken"),
]