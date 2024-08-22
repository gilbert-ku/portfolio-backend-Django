from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field



import uuid  #is used to generate uniq id

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key= True, editable=False, default=uuid.uuid4)

    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    updated_time = models.TimeField(auto_now=True)


    class Meta:
        abstract = True

class Blogs(BaseModel):
    user = models.ForeignKey(
        User, on_delete= models.CASCADE, null=False, blank=False
    )

    title = models.CharField(max_length=3000)
    image = models.ImageField(upload_to= "blog/blogpost")
    blog_text = models.TextField(max_length=3000, null=True, blank=True)
    # blog_body = CKEditor5Field()
    blog_body =  CKEditor5Field()
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
    
