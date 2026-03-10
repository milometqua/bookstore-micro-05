from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=200)