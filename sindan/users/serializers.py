from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    A serializer for `users.models.User` model.
    """
    class Meta:
        model = User

        exclude = (
            # exclude admin fields
            'is_staff',
            'is_active',
            'is_superuser',
        )
        read_only_fields = (
            'username',
            'date_joined',
            'last_login',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        request = self.context.get('request', None)

        # Enable editing `username` field if it's POST request and remove
        # `password` field if it's not.
        #
        # Reminder:
        #   password reset should be done via password reset API, because
        #   it requires using email validation stuff.
        if request and request.method == 'POST':
            fields['username'].read_only = False
        else:
            fields.pop('password')
        return fields


class UserSerializerWithPassword(serializers.ModelSerializer):
    """
    NOTE: FOR TESTING PURPOSE ONLY, AND MUST NOT BE USED
          EVER EXCEPT IN TESTING FILES.

    This is needed because 'CreateUserSerializer' doesn't
    serialize given password due 'write_only' attribute
    """
    class Meta:
        model = User

        exclude = (
            # exclude admin fields
            'is_staff',
            'is_active',
            'is_superuser',
        )
        read_only_fields = (
            'date_joined',
            'last_login',
        )
