import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # modified
    email = models.EmailField(unique=True)
    # added
    key = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
