from apps.auth.application.use_cases.user_auth_use_case import UserAuthUseCase
from rest_framework.viewsets import ViewSet
from apps.auth.infrastructure.factories.auth_use_case_factory import AuthUseCaseFactory
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.auth.infrastructure.mappers.user_mapper import UserMapper

class UsersViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def build_use_case(self) -> UserAuthUseCase:
        return AuthUseCaseFactory.build()

    def list(self, request):
        use_case = self.build_use_case()
        users = use_case.get_all_users()
        return Response([UserMapper.entity_to_dict(user) for user in users])
