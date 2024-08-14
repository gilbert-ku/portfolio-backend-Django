from django.db import models
from django.contrib.auth.models import User
# from PIL import Image

import uuid


# Create conact model


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now_add=True)
    # update_at = models.DateField(auto_add=True)


    class Meta:
        abstract = True



class Projects(BaseModel):
    user = models.ForeignKey(
        User, on_delete= models.CASCADE, null=False, blank=False
    )

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to= "projects/images")
    desctiption = models.TextField(max_length=500)
    url_link = models.URLField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    # class Meta:
    #     order_with_respect_to = "user"

