from django.db import models
import uuid
from utils.upload_file import upload_to_timestamp
from functools import partial
# Create your models here.


class Banner(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
    url = models.ImageField(upload_to=partial(upload_to_timestamp, 'banners/'))

    def __str__(self):
        return str(self.url)

    class Meta:
        db_table = 'banners'
