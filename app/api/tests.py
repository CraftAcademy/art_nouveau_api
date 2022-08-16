from urllib import request
from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

factory = APIRequestFactory()
user = User.objects.get(
    username='test')


def test_response(self):
    request = factory.get('/users/')
    force_authenticate(request, user=user)
    response = view(request)
