from apps.auth.application.dtos.user_dto import UserDTO
from apps.auth.domain.entities.user_entity import UserEntity


class UserMapper:
    @staticmethod
    def dto_to_entity(entity: UserDTO) -> UserEntity:
        return UserEntity(
            email=entity.email,
            password_hash=entity.password,
            first_name=entity.first_name,
            last_name=entity.last_name,
            picture=entity.picture,
        )
