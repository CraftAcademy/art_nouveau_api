import factory
from api.models import Project


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project
    title = "Foo"
    description = "Bar"
