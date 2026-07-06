from apps.auth.application.use_cases.user_auth_use_case import UserAuthUseCase
from apps.auth.domain.policies.login_policy import UserMustBeActive
from apps.auth.infrastructure.repositories.user_repository import (
    UserRepository,
)
from apps.auth.infrastructure.services.hasher_service import HasherService
from apps.auth.infrastructure.services.jwt_token_generator_service import (
    JWTTokenGeneratorService,
)


class AuthUseCaseFactory:
    @staticmethod
    def build() -> UserAuthUseCase:
        return UserAuthUseCase(
            token_service=JWTTokenGeneratorService(),
            user_repository=UserRepository(),
            hasher_service=HasherService(),
            policies=[UserMustBeActive()],
        )
