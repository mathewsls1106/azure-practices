from abc import ABC, abstractmethod

from apps.auth.domain.entities.user_entity import UserEntity


class IUserRepository(ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> UserEntity: ...

    @abstractmethod
    def create(self, entity: UserEntity) -> UserEntity: ...
