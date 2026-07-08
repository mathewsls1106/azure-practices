from dataclasses import dataclass
from typing import Any


@dataclass
class UserDTO:
    email: str
    first_name: str
    last_name: str
    password: str

    picture: Any | None = None
