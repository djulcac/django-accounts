from django.urls import path
from knox.views import LogoutAllView, LogoutView

from . import views

urlpatterns = [
    path('login/', views.LoginAPI.as_view()),
    path('logout/', LogoutView.as_view()),
    path('logoutall/', LogoutAllView.as_view()),
]
