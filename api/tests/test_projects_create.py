from rest_framework.test import APITestCase, APIClient

from api.models import Project
from .factories.project import ProjectFactory
from .factories.user import UserFactory
from django.contrib.auth.models import User

class CreateProject(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_data = {"title": "Real Project",
                           "description": "Lorem ipsum"}

    def test_as_an_unauthenticated_user(self):
        """ 
        returns 'forbidden' for unauthenticated user
        """
        request = self.client.post(
            '/projects/', self.valid_data, format='json')
        self.assertEquals(403, request.status_code)
        self.assertEquals(len(Project.objects.all()), 0)

    def test_as_an_authenticated_user(self):
        """
        creates an instance of 'Project' if user is authenticated
        """
        user = UserFactory(username="Thomas")
        # user = User.objects.get(username="Thomas")
        # self.client.login(username='Thomas', password='password')
        self.client.force_login(user=user)
        request = self.client.post(
            '/projects/', self.valid_data, format='json')
        self.assertEquals(201, request.status_code)
        self.assertEquals(len(Project.objects.all()), 1)
