from django.db import models
from functools import partial
from utils.upload_file import upload_to_timestamp
import uuid
# Create your models here.


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    website = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to=partial(
        upload_to_timestamp, 'company_logo/'), null=True, blank=True)
    employee_count = models.PositiveIntegerField(blank=True, null=True)
    benefits = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'companys'
