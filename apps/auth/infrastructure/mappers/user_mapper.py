from apps.auth.application.dtos.user_dto import UserDTO
from apps.auth.domain.entities.user_entity import UserEntity
from apps.auth.infrastructure.models.user_model import User


class UserMapper:
    @staticmethod
    def model_to_entity(model: User) -> UserEntity:
        return UserEntity(
            id=model.id,
            email=model.email,
            password_hash=model.password,
            first_name=model.first_name,
            last_name=model.last_name,
            is_active=model.is_active,
            picture=model.picture,
        )

    @staticmethod
    def entity_to_model(entity: UserEntity) -> User:
        return User(
            id=entity.id,
            email=entity.email,
            password=entity.password_hash,
            first_name=entity.first_name,
            last_name=entity.last_name,
            is_active=entity.is_active,
            picture=entity.picture,
        )

    @staticmethod
    def dict_to_dto(user_dict: dict) -> UserDTO:
        return UserDTO(
            email=user_dict["email"],
            password=user_dict["password"],
            first_name=user_dict["first_name"],
            last_name=user_dict["last_name"],
            picture=user_dict["picture"] if "picture" in user_dict else None,
        )
