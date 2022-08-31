import factory
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = "RandomGuy"
    email = "random_guy@email.com"
    password = "password"
