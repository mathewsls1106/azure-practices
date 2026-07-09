from apps.auth.application.dtos.user_dto import UserDTO
from apps.auth.application.mappers.user_mapper import UserMapper
from apps.auth.application.ports.repositories.i_user_repository import IUserRepository
from apps.auth.application.ports.services.i_password_hasher_service import (
    IPasswordHasherService,
)
from apps.auth.application.ports.services.i_token_generator_service import (
    ITokenGeneratorService,
)
from apps.auth.domain.exceptions.login_exception import (
    InvalidCredentialsException,
)
from apps.shared.application.validation import ensure_exists
from apps.shared.domain.policies.domain_policy import DomainPolicy
from apps.auth.domain.entities.user_entity import UserEntity


class UserAuthUseCase:
    def __init__(
        self,
        user_repository: IUserRepository,
        hasher_service: IPasswordHasherService,
        token_service: ITokenGeneratorService,
        policies: list[DomainPolicy] | None,
    ):
        self.user_repository = user_repository
        self.hasher_service = hasher_service
        self.token_service = token_service
        self.policies = policies or []

    def login(self, email: str, password: str) -> dict:
        user = self.user_repository.get_by_email(email)
        user = ensure_exists(user, InvalidCredentialsException())

        for policy in self.policies:
            policy.validate(user)

        if not self.hasher_service.check_password(password, user.password_hash):
            raise InvalidCredentialsException()

        return self.token_service.create_token(user)

    def register(self, user_dto: UserDTO) -> dict:
        user = self.user_repository.get_by_email(user_dto.email)

        if user:
            raise InvalidCredentialsException()

        password = user_dto.password
        user_dto.password = self.hasher_service.hash_password(password)

        user = UserMapper.dto_to_entity(user_dto)

        self.user_repository.create(user)

        return self.token_service.create_token(user)


    def get_all_users(self) -> list[UserEntity]:
        return self.user_repository.get_all()
