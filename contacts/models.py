from django.db import models
from django.contrib.auth.models import User

# Create conact model

class Contacts(models.Models):
    user = models.ForeignKey(
        User, on_delete= models.CASCADE, null=False, blank=True
    )

    full_name = models.CharField(max_length=100)
    # phone_number = models.(max_length=100)
