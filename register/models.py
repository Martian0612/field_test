from django.db import models

# Create your models here.
class CustomUserModel(models.Model):
    profile_photo = models.ImageField(null= True, blank = True, upload_to= "images/" )
    resume = models.FileField(null= True, blank = True, upload_to="file/documents/")
    
