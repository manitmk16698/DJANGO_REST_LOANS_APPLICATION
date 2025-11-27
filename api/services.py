from api.models import Role
from django.shortcuts import get_object_or_404

class RoleService:

    @staticmethod
    def create_role(validated_data):
        return Role.objects.create(**validated_data)

    @staticmethod
    def list_roles():
        return Role.objects.all().order_by('-id')

    @staticmethod
    def get_role_by_id(role_id):
        return get_object_or_404(Role, id=role_id)

    @staticmethod
    def update_role(role_instance, validated_data):
        for attr, value in validated_data.items():
            setattr(role_instance, attr, value)
        role_instance.save()
        return role_instance

    @staticmethod
    def delete_role(role_instance):
        role_instance.delete()
        return True
