from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User   # or settings.AUTH_USER_MODEL

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    disease = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
