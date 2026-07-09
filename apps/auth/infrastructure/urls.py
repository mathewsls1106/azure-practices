from django.urls import path, include

from apps.auth.infrastructure.views.login_view import LoginView
from apps.auth.infrastructure.views.register_view import RegisterView
from apps.auth.infrastructure.views.users_viewset import UsersViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"users", UsersViewSet, basename="users")

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("", include(router.urls)),
]
