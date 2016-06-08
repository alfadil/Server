from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from sindan.users.models import User


class AccountTests(APITestCase):

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('api:user-list')
        data = {'username': 'testuser',
                'email': 'dump@gmail.com', 'first_name': 'ali'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get(id=1).first_name, 'ali')
