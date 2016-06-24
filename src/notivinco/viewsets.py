from rest_framework import (
    filters,
    status,
    viewsets
)

from .models import *  # flake8: noqa

from .serializers import *  # flake8: noqa

class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()

class NoticesViewSet(viewsets.ModelViewSet):
    serializer_class = NoticesSerializer
    queryset = Notice.objects.all()

class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    queryset = Comment.objects.all()