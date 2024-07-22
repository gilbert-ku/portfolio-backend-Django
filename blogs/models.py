from django.db import models


import uuid  #is used to generate uniq id

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key= True, editable=False, default=uuid.uuid4)

    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    updated_time = models.TimeField(auto_now_add=True)


    class Meta:
        abstract = True


