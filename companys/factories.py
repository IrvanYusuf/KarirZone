# jobs/factories.py
import factory
from faker import Faker
from .models import Company
import uuid

fake = Faker('id_ID')  # lokal Indonesia


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.LazyAttribute(lambda x: f"{fake.company()}")
    website = factory.LazyAttribute(lambda x: fake.url())
    location = factory.LazyAttribute(lambda x: fake.city())
    description = factory.LazyAttribute(lambda x: fake.text(max_nb_chars=200))
    employee_count = factory.LazyAttribute(
        lambda x: fake.random_int(min=10, max=5000))
    benefits = factory.LazyAttribute(lambda x: ", ".join(fake.words(nb=3)))
    email = factory.LazyAttribute(lambda x: fake.company_email())
