from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from sindan.users.models import User
from sindan.users.factories import UserFactory
from sindan.users.serializers import UserSerializerWithPassword


class UserTests(APITestCase):

    def test_create_user(self):
        u = UserFactory.build(username="fakeuser", password="superstrong")
        s = UserSerializerWithPassword(u)
        print(s.data)
        url = reverse('api:user-list')

        response = self.client.post(url, s.data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertNotEqual(User.objects.get(id=1).password, 'superstrong')

    def test_update_user(self):
        u = UserFactory.create(first_name="first_test")

        url = reverse('api:user-detail', args=[u.username])
        data = {'first_name': 'second_test'}

        response = self.client.patch(url, data)
        u.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(u.first_name, 'second_test')

    def test_delete_user(self):
        u = UserFactory.create(is_active=True)

        url = reverse('api:user-detail', args=[u.username])
        response = self.client.delete(url)
        u.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(u.is_active, False)
