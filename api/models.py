from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    published=models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-published']