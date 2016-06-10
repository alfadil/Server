import factory
from factory.django import DjangoModelFactory
from . import models


class UserFactory(DjangoModelFactory):

    class Meta:
        model = models.User

    username = factory.Faker('user_name')
    email = factory.LazyAttribute(
        lambda a: '{0}.{1}@example.com'.format(
            a.first_name, a.last_name
        ).lower()
    )
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True
    is_staff = False
    is_superuser = False
    password = factory.Faker('password')
