from dataclasses import dataclass


@dataclass(frozen=True)
class FileFieldVO:
    content: bytes
    url: str
    size: int
