from rest_framework import serializers
from .models import User


class ListUserSerializer(serializers.ModelSerializer):
    """
    List all fields of User model except excluded ones
    """

    class Meta:
        model = User
        exclude = (
            'password',
        )


class CreateUserSerializer(serializers.ModelSerializer):
    """
    Required fields are: username, email, password
    """

    class Meta:
        model = User
        exclude = (
            'is_active',
            'date_joined',
            'last_login',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UpdateUserSerializer(serializers.ModelSerializer):
    """
    Required fields are: nothing
    """

    class Meta:
        model = User
        exclude = (
            'username',
            'is_active',
            'date_joined',
            'last_login',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, user, validated_data):
        for attr, value in validated_data.items():
            setattr(user, attr, value)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializerWithPassword(CreateUserSerializer):
    """
    NOTE: FOR TESTING PURPOSE ONLY, AND MUST NOT BE USED
          EVER EXCEPT IN TESTING FILES.

    This is needed because 'CreateUserSerializer' doesn't
    serialize given password due 'write_only' attribute
    """
    class Meta:
        model = User
        exclude = (
            'is_active',
            'date_joined',
            'last_login',
        )
