from django.db import models
from django.contrib.auth.models import User


# Create conact model

class Contacts(models.Model):
    user = models.ForeignKey(
        User, on_delete= models.CASCADE, null=False, blank=False
    )

    title = models.CharField(max_length=100)
    image = models.ImageField()
    desctiption = models.TextField(max_length=500)
    url_link = models.URLField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    # class Meta:
    #     order_with_respect_to = "user"

