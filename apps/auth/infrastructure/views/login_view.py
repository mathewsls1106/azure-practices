from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.auth.application.use_cases.user_auth_use_case import UserAuthUseCase
from apps.auth.domain.exceptions.login_exception import InvalidCredentialsException
from apps.auth.infrastructure.factories.auth_use_case_factory import (
    AuthUseCaseFactory,
)
from apps.auth.infrastructure.helpers.cookie_helper import (
    set_refresh_cookie,
)
from apps.auth.infrastructure.serializers.user_serializers import (
    LoginUserSerializer,
)


class LoginView(APIView):
    def build_use_case(self) -> UserAuthUseCase:
        return AuthUseCaseFactory.build()

    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        use_case = self.build_use_case()
        try:
            token_dict = use_case.login(
                email=serializer.validated_data["email"],
                password=serializer.validated_data["password"],
            )
            access_token = token_dict["access"]
            refresh_token = token_dict["refresh"]
            response = Response(
                {"access_token": access_token}, status=status.HTTP_200_OK
            )
            set_refresh_cookie(response, refresh_token)
            return response
        except InvalidCredentialsException:
            return Response(
                {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
