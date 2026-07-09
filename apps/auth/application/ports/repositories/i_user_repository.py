from abc import ABC, abstractmethod

from typing import List

from apps.auth.domain.entities.user_entity import UserEntity


class IUserRepository(ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> UserEntity | None: ...

    @abstractmethod
    def create(self, entity: UserEntity) -> UserEntity: ...

    @abstractmethod
    def get_all(self) -> List[UserEntity]: ...
