from rest_framework_simplejwt.tokens import RefreshToken

from apps.auth.application.ports.services.i_token_generator_service import (
    ITokenGeneratorService,
)
from apps.auth.domain.entities.user_entity import UserEntity
from apps.auth.infrastructure.mappers.user_mapper import UserMapper


class JWTTokenGeneratorService(ITokenGeneratorService):
    def create_token(self, user: UserEntity) -> dict:

        user = UserMapper.entity_to_model(user)

        refresh = RefreshToken.for_user(user)

        refresh["user_id"] = user.id
        refresh["email"] = user.email

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
