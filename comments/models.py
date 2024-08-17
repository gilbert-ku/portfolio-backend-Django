from django.db import models
# from projects.models import Projects
from blogs.models import Blogs


import uuid


class BaseModel(models.Model):

    # create prmary key
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    #  add tine stamp
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    updated_time = models.TimeField(auto_now=True)


    class Meta:
        abstract = True

class Comments(models.Model):
    # foriegn key
    Blogs = models.ForeignKey(
        Blogs, on_delete= models.CASCADE, null=False, blank= False
    )

    # fields
    comments = models.TextField(max_length=1000, null=True, blank=True)
    like = models.BooleanField(default=False)

    def __str__(self):
        return self.comments
