from django.db import models


class Prod1(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=20)

    class Meta:
        db_table = 'prod1'

