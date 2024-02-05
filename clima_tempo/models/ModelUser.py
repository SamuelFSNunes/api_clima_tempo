from django.db import models

class ModelUser(models.Model):
  name = models.CharField(blank=False, null=False, max_length=50)
  email = models.EmailField(blank=False, null=False, unique=True, max_length=100)
  password = models.CharField(blank=False, null=False, max_length=50)

  def __str__(self):
    return f"{self.name}"