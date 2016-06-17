from rest_framework import serializers
from .models import User
from . import validators


class UserSerializer(serializers.ModelSerializer):
    """
    A serializer for `users.models.User` model.
    """
    confirm_password = serializers.CharField(
        write_only=True,
        max_length=128,
        min_length=8,
        required=True
    )

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
        extra_kwargs = {
            'username': {'validators': [validators.username_validator]},
            'email': {'validators': [validators.email_validator]},
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # remove confirm_password field
        validated_data.pop('confirm_password')

        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, data):
        """
        Extra validation
        """
        validators.passwords_match(data)
        return data

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
            fields.pop('confirm_password')
        return fields
