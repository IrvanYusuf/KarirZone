from django.db import models
import uuid
from companys.models import Company

# Create your models here.


class Job(models.Model):
    id = models.UUIDField(primary_key=True, max_length=36,
                          default=uuid.uuid4(), editable=False)
    title = models.CharField(max_length=255)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='jobs')
    salary = models.IntegerField(default=0)
    location = models.CharField(max_length=100)
    requirements = models.TextField()
    description = models.TextField()
    is_remote = models.BooleanField(default=False)
    posted_at = models.DateTimeField(auto_now_add=True)
    is_open = models.BooleanField(default=True)

    class Meta:
        db_table = 'jobs'
