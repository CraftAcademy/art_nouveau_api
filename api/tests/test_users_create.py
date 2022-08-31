from rest_framework.test import APITestCase


class UserCreateTest(APITestCase):
    def test_responds_with_user_created(self):
        data = {"username": "RealUser",
                "email": "test@email.com", "password": "password"}
        request = self.client.post(
            '/users/', data, format='json')
        self.assertEquals(201, request.status_code)
