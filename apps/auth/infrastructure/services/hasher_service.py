from django.contrib.auth.hashers import check_password, make_password

from apps.auth.application.ports.services.i_password_hasher_service import (
    IPasswordHasherService,
)


class HasherService(IPasswordHasherService):
    def check_password(self, password: str, password_hash: str) -> bool:
        return check_password(password, password_hash)

    def hash_password(self, password: str) -> str:
        return make_password(password)
