from apps.auth.domain.entities.user_entity import UserEntity
from apps.auth.domain.exceptions.login_exception import UserIsNotActiveException
from apps.shared.domain.policies.domain_policy import DomainPolicy


class UserMustBeActive(DomainPolicy):
    def validate(self, candidate: UserEntity):
        if not candidate.is_active:
            raise UserIsNotActiveException()
