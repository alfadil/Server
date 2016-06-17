from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from sindan.users.models import User
from sindan.users.factories import UserFactory
from sindan.users.serializers import UserSerializer


class UserTests(APITestCase):

    def test_create_user(self):
        u = UserFactory.build(username="fakeuser")
        s = UserSerializer(u)
        data = s.data

        data['password'] = 'superstrong'
        data['confirm_password'] = data['password']

        url = reverse('api:user-list')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertNotEqual(User.objects.get(id=1).password, 'superstrong')

    def test_create_invalid_user(self):
        url = reverse('api:user-list')
        u = UserFactory.build(username="invalide user name")
        s = UserSerializer(u)
        data = s.data

        data['password'] = 'password'
        data['confirm_password'] = data['password']

        # invalid username
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # invalid username length
        data['username'] = 'short'
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # password match
        data['username'] = 'validusername'
        data['confirm_password'] = "doesn't match"
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_duplicate_username(self):
        url = reverse('api:user-list')
        # exists username
        u = UserFactory.create(username="testuser")
        s = UserSerializer(u)
        data = s.data
        data['password'] = 'password'
        data['confirm_password'] = data['password']
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

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

    def test_get_full_name(self):
        u = UserFactory.create()
        full = "{} {}".format(u.first_name, u.last_name)

        self.assertEqual(u.get_short_name(), u.first_name)
        self.assertEqual(u.get_full_name(), full)
