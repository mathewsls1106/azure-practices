from abc import ABC, abstractmethod


class IPasswordHasherService(ABC):
    @abstractmethod
    def check_password(self, password: str, password_hash: str) -> bool: ...

    @abstractmethod
    def hash_password(self, password: str) -> str: ...
