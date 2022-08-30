from rest_framework.test import APITestCase, APIRequestFactory


class UserCreateTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
    #     user = User.objects.create_superuser(
    #         username='test', email='test@email.com', password='password')
    #     user = User.objects.get(username='test')
    #     self.client.force_authenticate(user=user)

    def test_responds_with_user_created(self):
        data = {"username": "Real User",
                "email": "test@email.com", "password": "password"}
        # response = self.factory.post('http://testserver/users/', data, format='json')
        # breakpoint()
        response = self.client.post(
            '/users/', data, format='json')
        self.assertEquals(201, response.status_code)
