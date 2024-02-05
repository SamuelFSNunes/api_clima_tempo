from django.db import models

class ModelEntity(models.Model):
  CONDITION_CHOICES = [
    ("1", "Ensolarado"),
    ("2", "Chuvoso"),
    ("3", "Nublado"),
    ("4", "Úmido"),
    ("5", "Trovejando"),
  ]
  temperature = models.FloatField(blank=True, null=True)
  atmoatmospheric = models.FloatField(blank=True, null=True)
  humidity = models.FloatField(blank=True, null=True)
  precipitation = models.FloatField(blank=True, null=True)
  condition = models.CharField(max_length=1,blank=False, null=False, choices=CONDITION_CHOICES)

  def __str__(self):
    return "Conditions"
    