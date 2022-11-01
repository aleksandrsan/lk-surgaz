import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from contragents.models import Client

class CustomUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
