from abc import ABC, abstractmethod
from typing import Any


class ITokenGeneratorService(ABC):
    @abstractmethod
    def create_token(self, user: Any) -> dict: ...
