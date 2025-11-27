from django.db import models
from django.contrib.auth.models import AbstractUser

# from django.contrib.auth.models import AbstractUser
from django.db import models

import uuid
# from django.db import models

class Role(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    # FIX: override the M2M fields to avoid reverse accessor clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='api_user_groups',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='api_user_permissions',
        blank=True
    )

    def __str__(self):
        return f"{self.username} ({self.role})"


