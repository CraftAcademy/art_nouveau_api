from rest_framework.test import APITestCase
from .factories.project import ProjectFactory


class ProjectsIndexTest(APITestCase):
    def setUp(self):
        ProjectFactory()

    def test_list_projects(self):
        response = self.client.get('http://testserver/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Foo')
        self.assertEqual(response.data[0]['description'], 'Bar')
