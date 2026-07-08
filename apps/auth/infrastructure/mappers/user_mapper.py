from django.core.files.base import File
from django.forms.fields import FileField

from apps.auth.application.dtos.user_dto import UserDTO
from apps.auth.domain.entities.user_entity import UserEntity
from apps.auth.infrastructure.models.user_model import User
from apps.shared.infrastructure.mappers.file_field_mapper import FileFieldMapper


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
            picture=FileFieldMapper.file_field_to_vo(model.picture),
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
            picture=FileFieldMapper.vo_to_file_field(entity.picture),
        )

    @staticmethod
    def dict_to_dto(user_dict: dict) -> UserDTO:
        return UserDTO(
            email=user_dict["email"],
            password=user_dict["password"],
            first_name=user_dict["first_name"],
            last_name=user_dict["last_name"],
            picture=FileFieldMapper.file_field_to_vo(
                user_dict.get("picture") if user_dict.get("picture") else None
            ),
        )
