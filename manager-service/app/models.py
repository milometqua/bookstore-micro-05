from django.db import models

class Manager(models.Model):
    name = models.CharField(max_length=200)