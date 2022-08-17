from rest_framework.test import APITestCase


class ProjectsIndexTest(APITestCase):
    def setUp(self):
        valid_data = {'title': 'test', 'description': 'test'}
        

    def test_list_projects(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)
