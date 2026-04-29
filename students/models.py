from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=77)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(max_length=10)

    def __str__(self):
        return self.email
    