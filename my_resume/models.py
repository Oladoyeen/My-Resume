from django.db import models

# Create your models here.
class Contact(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.EmailField()
    Message=models.TextField()
    def __str__(self) -> str:
        return self.name

