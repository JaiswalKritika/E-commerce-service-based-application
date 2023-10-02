from django.db import models
from tinymce.models import HTMLField

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)


class catego(models.Model):
    title = models.CharField(max_length=255)
    description = HTMLField(null=True)
    image = models.FileField(upload_to="images/",max_length=255,null=True,default=None)
    created_date=models.DateTimeField(null=True)
    updated_date=models.DateTimeField(null=True)

class SubCatego(models.Model):
    category_Id=models.ForeignKey(catego, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = HTMLField(null=True)
    Subcategory_image=models.ImageField(upload_to="category/",max_length=250,null=True,default=None)
    created_date=models.DateTimeField(null=True)
    updated_date=models.DateTimeField(null=True)
    
    def __str__(self):
        return self.title