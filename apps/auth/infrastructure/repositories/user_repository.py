from apps.auth.application.ports.repositories.i_user_repository import IUserRepository
from apps.auth.domain.entities.user_entity import UserEntity
from apps.auth.infrastructure.mappers.user_mapper import UserMapper
from apps.auth.infrastructure.models.user_model import User


class UserRepository(IUserRepository):
    model = User

    def get_by_email(self, email: str) -> UserEntity | None:
        model = self.model.objects.filter(email=email).first()

        if not model:
            return None

        return UserMapper.model_to_entity(model)

    def create(self, entity: UserEntity) -> UserEntity:
        model = UserMapper.entity_to_model(entity)
        model.save()
        return UserMapper.model_to_entity(model)


    def get_all(self) -> list[UserEntity]:
        models = self.model.objects.all()
        return [UserMapper.model_to_entity(model) for model in models]
