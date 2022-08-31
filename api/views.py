from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import ProjectSerializer, UserSerializer, GroupSerializer
from api.models import Project
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        permission_classes = [permissions.AllowAny]
        if not self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        
        return [permission() for permission in permission_classes]

    def list(self):
        breakpoint()
        queryset = self.get_queryset()
        serializer = ProjectSerializer(queryset, many=True)
        return Response({'projects': serializer.data})

