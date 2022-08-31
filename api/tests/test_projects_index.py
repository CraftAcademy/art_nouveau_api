from rest_framework.test import APITestCase, APIClient
from .factories.project import ProjectFactory


class ProjectsIndexTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        ProjectFactory()

    def test_list_projects(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        project = response.data['projects'][0]
        self.assertEqual(project['title'], 'Foo')
        self.assertEqual(project['description'], 'Bar')
        self.assertTrue(project['id'])
