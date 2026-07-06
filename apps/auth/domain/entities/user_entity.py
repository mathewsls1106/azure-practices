from dataclasses import dataclass

from apps.auth.domain.value_objects.file_field_vo import FileFieldVO


@dataclass
class UserEntity:
    email: str
    password_hash: str
    first_name: str
    last_name: str

    picture: FileFieldVO | None = None
    id: int | None = None
    is_active: bool = True

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
