import eav
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=20,decimal_places=4)

    def __unicode__(self):
        return self.title


eav.register(Product)


