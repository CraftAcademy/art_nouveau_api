import factory
from api.models import Project


class ProjectFactory(factory.Factory):
    class Meta:
        model = Project
    title = "Foo"
    description = "Bar"
