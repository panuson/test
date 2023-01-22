from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.TextField()
    content = models.TextField()
    writer = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)


    

    