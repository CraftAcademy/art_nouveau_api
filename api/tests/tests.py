from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class Testing(APITestCase):
    def setUp(self):
        user = User.objects.create_superuser(
            username='test', email='test@email.com', password='password')
        user = User.objects.get(username='test')
        self.client.force_authenticate(user=user)

    def test_responds_with_list_of_users(self):
        response = self.client.get('http://testserver/users/')
        self.assertEquals(200, response.status_code)
