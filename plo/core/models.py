from django.db import models

# Create your models here.

class Fields(models.Model):
    id = models.AutoField(primary_key=True)
    selections = models.JSONField(default=list)