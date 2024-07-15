from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create conact model

class Contacts(models.Model):
    user = models.ForeignKey(
        User, on_delete= models.CASCADE, null=False, blank=False
    )

    full_name = models.CharField(max_length=100)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
    # class Meta:
    #     order_with_respect_to = "user"

