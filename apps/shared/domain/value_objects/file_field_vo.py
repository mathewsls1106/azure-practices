from dataclasses import dataclass


@dataclass(frozen=True)
class FileFieldVO:
    content: bytes
    name: str
    size: int
