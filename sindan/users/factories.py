import factory
from factory.django import DjangoModelFactory
from . import models


class UserFactory(DjangoModelFactory):

    class Meta:
        model = models.User

    username = factory.Faker('user_name')
    email = factory.LazyAttribute(
        lambda f: '{0}.{1}@example.com'.format(
            f.first_name, f.last_name
        ).lower()
    )
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True
    is_staff = False
    is_superuser = False
    password = factory.PostGenerationMethodCall(
        'set_password',
        factory.Faker('password')
    )
