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
from apps.auth.infrastructure.mappers.user_mapper import UserMapper
from apps.auth.infrastructure.serializers.user_serializers import (
    CreateUserSerializer,
)


class RegisterView(APIView):
    def build_use_case(self) -> UserAuthUseCase:
        return AuthUseCaseFactory.build()

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        use_case = self.build_use_case()
        user_dto = UserMapper.dict_to_dto(serializer.validated_data)
        try:
            tokens = use_case.register(user_dto)
            access_token = tokens["access"]
            refresh_token = tokens["refresh"]

            response = Response(
                {"access_token": access_token}, status=status.HTTP_201_CREATED
            )
            set_refresh_cookie(response, refresh_token)
            return response

        except InvalidCredentialsException:
            return Response(
                {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
