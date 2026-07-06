from dataclasses import dataclass


@dataclass(frozen=True)
class FileFieldVO:
    url: str
    name: str
    size: int
