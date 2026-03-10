from django.db import models

class Shipment(models.Model):
    order_id = models.IntegerField()
    address = models.CharField(max_length=200)