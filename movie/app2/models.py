from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=20)
    director=models.CharField(max_length=20)
    image=models.FileField(upload_to="image",null=True,blank=True)
    def __str__(self):
        return self.title