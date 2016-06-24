from .models import * # flake8: noqa
from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = (
            'id',
            'email',
            'password',
            'name',
            'last_name',
            'is_superuser',
            'is_staff',
            'is_active'
        )


class NoticesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notice
        fields = (
        	'id',
        	'title',
        	'content',
        	'is_active',
        	'user'
        )


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
        	'id',
        	'comment',
        	'is_active',
        	'notice',
        	'user'
        )

