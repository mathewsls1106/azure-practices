from abc import ABC, abstractmethod


class ITokenGeneratorService(ABC):
    @abstractmethod
    def create_token(self, user: any) -> str: ...
