from dataclasses import dataclass


@dataclass
class UserDTO:
    email: str
    first_name: str
    last_name: str
    picture: str
    password: str
