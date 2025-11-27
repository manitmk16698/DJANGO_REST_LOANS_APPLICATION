from django.urls import path

from api.views import (
    RoleListCreateAPIView,
    RoleRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('roles/', RoleListCreateAPIView.as_view(), name='role-list-create'),
    path('roles/<str:pk>/', RoleRetrieveUpdateDestroyAPIView.as_view(), name='role-detail'),
]
