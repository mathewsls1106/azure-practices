from abc import ABC, abstractmethod


class DomainPolicy(ABC):
    @abstractmethod
    def validate[T](self, candidate: T) -> None: ...
