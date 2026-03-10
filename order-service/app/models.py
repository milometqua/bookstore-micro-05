from django.db import models

class Order(models.Model):
    customer_id = models.IntegerField()
    total_price = models.FloatField()
    status = models.CharField(max_length=50, default="pending")
