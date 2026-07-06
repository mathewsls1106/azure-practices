from django.urls import path

from apps.auth.infrastructure.views.login_view import LoginView
from apps.auth.infrastructure.views.register_view import RegisterView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
]
