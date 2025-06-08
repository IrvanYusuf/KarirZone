# jobs/factories.py
import factory
from faker import Faker
from .models import Job
import uuid
from companys.models import Company

fake = Faker('id_ID')  # lokal Indonesia


class JobFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Job

    id = factory.LazyFunction(uuid.uuid4)
    title = factory.LazyAttribute(lambda x: fake.job())
    company = factory.Iterator(Company.objects.all())
    salary = factory.LazyAttribute(
        lambda x: fake.random_int(min=3000000, max=30000000))
    location = factory.LazyAttribute(
        lambda x: f"{fake.city()}, {fake.state()}")
    requirements = factory.LazyAttribute(
        lambda x: "\n".join(fake.sentences(nb=3)))
    description = factory.LazyAttribute(
        lambda x: "\n".join(fake.paragraphs(nb=3)))
    is_remote = factory.LazyAttribute(lambda x: fake.boolean())
    posted_at = factory.LazyAttribute(lambda x: fake.date_time_this_year())
