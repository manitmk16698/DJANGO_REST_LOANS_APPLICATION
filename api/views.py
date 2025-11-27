
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from api.serializers import RoleSerializer
from api.services import RoleService

class RoleListCreateAPIView(ListCreateAPIView):
    serializer_class = RoleSerializer

    def get_queryset(self):
        return RoleService.list_roles()

    def perform_create(self, serializer):
        RoleService.create_role(serializer.validated_data)


class RoleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RoleSerializer

    def get_object(self):
        role_id = self.kwargs.get("pk")
        return RoleService.get_role_by_id(role_id)

    def perform_update(self, serializer):
        instance = self.get_object()
        RoleService.update_role(instance, serializer.validated_data)

    def perform_destroy(self, instance):
        print("in delete")
        RoleService.delete_role(instance)
